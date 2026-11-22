"""Huawei ``visitPoint`` PTZ-preset service on cameras.

A camera Profile declares one ``visitPoint`` service per stored preset
(``visitPoint1`` … ``visitPoint12``), each with four characteristics:

    move   bool RW  1 = pan/tilt to the stored position, 0 = idle
    enable bool RW  1 = this preset has been configured by the user
    id     string    plugin-assigned identifier used by IFTTT matching
    name   string    user-given preset name

``move`` is a trigger, not a state: the camera reports 0 again once it has
arrived, and the Profile states that only one preset may be ``move=1`` at a
time. Exposing it as an HA ``button`` matches that behaviour exactly — press
once to go there, nothing to turn back off.

``enable`` is the only durable state, so it is exposed as a ``binary_sensor``
(``configured``). It is read-only here: the App writes it when the user stores
a preset, and writing it from HA would need coordinates the Profile never
carries.

contract
    field : characteristic used for the HA press (default ``move``)
"""

from __future__ import annotations

from ..models import ServiceRef

# Profiles in the wild use these two names for the trigger.
_TRIGGERS = ("move", "action")


class VisitPointServiceAdapter:
    service_id = "visitPoint1"
    # Huawei serviceType from the Profile; it is not always the sid.
    service_type = "visitPoint"
    # Declared for the UI entity selector; validate_entities enforces the same rule.
    entity_domains = ("button",)
    entity_counts = None

    def validate_service(self, service: ServiceRef) -> None:
        if service.service_type != "visitPoint":
            raise ValueError("visitPoint requires st: visitPoint")
        unknown = set(dict(service.contract)) - {"field"}
        if unknown:
            raise ValueError(
                "visitPoint has unsupported contract keys: "
                f"{', '.join(sorted(unknown))}"
            )
        field = service.contract_value("field")
        if field is not None and (not isinstance(field, str) or not field):
            raise ValueError("visitPoint contract field must be non-empty text")

    def validate_entities(self, entity_ids: tuple[str, ...]) -> None:
        if len(entity_ids) != 1:
            raise ValueError("visitPoint requires exactly one button entity")
        if not entity_ids[0].startswith("button."):
            raise ValueError("visitPoint requires a button entity")

    @staticmethod
    def _field(service: ServiceRef) -> str:
        explicit = service.contract_value("field")
        if isinstance(explicit, str) and explicit:
            return explicit
        return _TRIGGERS[0]

    async def read_state(
        self, hass, service: ServiceRef, entity_ids: tuple[str, ...]
    ) -> dict[str, object]:
        """A preset carries no durable state to report.

        ``move`` resets to 0 after the camera arrives and ``enable`` is written
        by the App, so reporting either as a live value would make HA fight the
        App. Nothing is published.
        """

        self.validate_service(service)
        self.validate_entities(entity_ids)
        return {}

    async def apply_command(
        self,
        hass,
        service: ServiceRef,
        entity_ids: tuple[str, ...],
        payload: dict[str, object],
    ) -> None:
        """Press the button: send ``move=1`` to the camera."""

        self.validate_service(service)
        self.validate_entities(entity_ids)
        field = self._field(service)
        if payload.get(field) not in {1, True, "1", "true"}:
            return
        domain = entity_ids[0].partition(".")[0]
        await hass.services.async_call(
            domain,
            "press",
            {"entity_id": entity_ids[0]},
            blocking=True,
        )


ADAPTER = VisitPointServiceAdapter()