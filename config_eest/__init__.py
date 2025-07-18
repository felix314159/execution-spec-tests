"""General purpose configuration system - all in one file"""

from types import SimpleNamespace
from typing import Any, Dict

# --------------------------------- do NOT modify ----------------------------------


class ConfigSystem:
    """General purpose config that can handle any namespace dynamically"""

    def __init__(self):
        self._namespaces: Dict[str, Dict[str, Any]] = {}
        self._proxies: Dict[str, Any] = {}

    def register_namespace(self, namespace: str, instances: Dict[str, Any]):
        """Register any namespace with its instances"""
        self._namespaces[namespace] = instances

        # Auto-generate proxy for this namespace
        proxy_class = self._create_proxy_class(namespace)
        proxy = SimpleNamespace(**{name.upper(): proxy_class(name) for name in instances})
        self._proxies[namespace] = proxy

        # Store proxy as attribute
        setattr(self, namespace.upper(), proxy)

    def _create_proxy_class(self, namespace: str):
        """Create a proxy class for a namespace"""

        class DynamicProxy:
            def __init__(self, item_name: str):
                self._namespace = namespace
                self._item = item_name

            def __getattr__(self, field: str):
                return f"{self._namespace}.{self._item}.{field.lower()}"

            def __str__(self):
                return f"{self._namespace}.{self._item}"

        return DynamicProxy

    def get(self, path: Any) -> Any:
        """Get config value from any path format - handles any depth"""
        # If it's not a string path, just return the value itself
        if not isinstance(path, str):
            return path

        path_str = str(path)
        parts = path_str.split(".")

        if not parts:
            raise ValueError("Empty path")

        # Start with the namespace
        namespace = parts[0]
        if namespace not in self._namespaces:
            # If it's a single part and not a namespace, it might be a raw value
            if len(parts) == 1:
                # Try to evaluate if it's a number
                try:
                    return int(path_str)
                except ValueError:
                    try:
                        return float(path_str)
                    except ValueError:
                        pass
            raise ValueError(f"Unknown namespace: {namespace}")

        # Get the current object starting from namespace
        current = self._namespaces[namespace]

        # Navigate through the path
        for i, part in enumerate(parts[1:], 1):
            if isinstance(current, dict):
                # Dictionary access
                if part in current:
                    current = current[part]
                else:
                    raise ValueError(f"Key '{part}' not found at level {i} in path: {path_str}")
            elif hasattr(current, part):
                # Object attribute access
                current = getattr(current, part)
            else:
                raise ValueError(f"Attribute '{part}' not found at level {i} in path: {path_str}")

        return current


# Create the config system instance
config_eest = ConfigSystem()


# --------------------------------- end of read-only ----------------------------------

# TODO: maintain below as you add complex config classes

# ----------------------- forks -------------------------------
from config_eest.forks_config.frontier_config import FrontierConfig
from config_eest.forks_config.homestead_config import HomesteadConfig

config_eest.register_namespace(
    "forks",
    {
        "frontier": FrontierConfig(),
        "homestead": HomesteadConfig(),
    },
)
FORKS = config_eest.FORKS  # type: ignore[attr-defined]

# ------------------------------------------------------------

__all__ = ["config_eest", "FORKS"]
