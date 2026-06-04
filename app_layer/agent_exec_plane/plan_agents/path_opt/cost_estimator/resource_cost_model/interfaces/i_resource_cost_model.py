from typing import Protocol


class IResourceCostModel(Protocol):
    def estimate_cpu(self, path: dict) -> float:
        ...

    def estimate_mem(self, path: dict) -> float:
        ...

    def estimate_io(self, path: dict) -> float:
        ...
