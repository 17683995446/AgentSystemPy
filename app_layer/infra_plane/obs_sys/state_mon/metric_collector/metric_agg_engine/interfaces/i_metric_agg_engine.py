from typing import Protocol


class IMetricAggEngine(Protocol):
    def aggregate_sum(self, samples: list[float]) -> float:
        ...

    def aggregate_avg(self, samples: list[float]) -> float:
        ...

    def aggregate_percentile(self, samples: list[float], p: float) -> float:
        ...
