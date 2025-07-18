# Clean enum implementation - zero duplication!


from types import SimpleNamespace
from typing import Any

from config.forks.frontier_config import FrontierConfig
from config.forks.homestead_config import HomesteadConfig

frontier = FrontierConfig()
homestead = HomesteadConfig()

# dict below is the only thing that has to manually be maintained here whenever new fork is added
_forks = {
    "frontier": frontier,
    "homestead": homestead,
}


class DynamicFork:
    """Fork that builds paths dynamically"""

    def __init__(self, name: str):
        self._name = name

    def __getattr__(self, field: str) -> str:
        return f"{self._name}.{field.lower()}"


FORKS = SimpleNamespace(**{name.upper(): DynamicFork(name) for name in _forks})


class Config:
    """Simple config accessor"""

    def get(self, path: str) -> Any:
        fork_name, field_name = path.split(".", 1)
        return getattr(_forks[fork_name], field_name)


config = Config()
