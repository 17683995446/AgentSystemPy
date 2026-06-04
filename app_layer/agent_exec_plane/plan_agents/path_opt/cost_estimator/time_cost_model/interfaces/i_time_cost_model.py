from typing import Protocol


class ITimeCostModel(Protocol):
    def estimate_latency(self, path: dict) -> float:
        ...

    def estimate_duration(self, path: dict) -> float:
        ...

    def estimate_deadline(self, path: dict) -> float:
        ...
