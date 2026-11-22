"""Hard-coded adapters, one for each supported Huawei service."""

from .registry import get_adapter_for_service, get_service_adapter

__all__ = ["get_adapter_for_service", "get_service_adapter"]
