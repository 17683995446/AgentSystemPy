from typing import Protocol


class ITaskSizeEstimator(Protocol):
    def estimate_complexity(self, task: dict) -> int:
        ...

    def estimate_time(self, task: dict) -> float:
        ...

    def estimate_memory(self, task: dict) -> int:
        ...
