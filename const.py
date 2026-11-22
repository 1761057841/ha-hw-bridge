from __future__ import annotations

DOMAIN = "ha_hw_bridge"

# Domains this integration used before the rename. Their stored gateway
# material is adopted once so paired gateways keep working.
LEGACY_DOMAINS = ("oneconnect_bridge",)

CONF_INTERFACE_IP = "interface_ip"
CONF_MAC = "mac"
CONF_SERIAL = "serial"
CONF_ENABLE_TRACE = "enable_trace"
# Shown only while a gateway paired under the pre-rename domain can be adopted.
CONF_REUSE_SERIAL = "reuse_serial"

VIRTUAL_HARDWARE_VERSION = "1.0.0"

DEFAULT_PRODUCT_ID = "ZG37"
DEFAULT_DEVICE_TYPE = "A17"
# Huawei cloud manufacturer ID used in the wire-level devInfo payload.
DEFAULT_MANUFACTURER = "002"
# Stable Python gateway identity; do not derive display metadata from a profile.
DEFAULT_MODEL = "HA-SCG-ZG37"
DEFAULT_PROTOCOL_TYPE = 1

GATEWAY_MANUFACTURER = "华为"

DISCOVERY_PORT = 5683
DISCOVERY_MULTICAST = "238.238.238.238"
PIN_TTL_SECONDS = 300

# Keep local/cloud abuse-prevention limits fixed.
MAX_GATEWAY_INSTANCES = 3
MAX_CHILD_DEVICES_PER_GATEWAY = 64