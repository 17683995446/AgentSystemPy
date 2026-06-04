from typing import Protocol


class IMetricSamplePool(Protocol):
    def add_sample(self, metric_id: str, value: float) -> None:
        ...

    def evict_oldest(self, metric_id: str) -> None:
        ...

    def compute_stats(self, metric_id: str) -> dict:
        ...
