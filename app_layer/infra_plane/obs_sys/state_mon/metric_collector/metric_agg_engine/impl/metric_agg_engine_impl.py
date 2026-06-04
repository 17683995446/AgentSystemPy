from ..interfaces.i_metric_agg_engine import IMetricAggEngine


class MetricAggEngineImpl(IMetricAggEngine):
    def aggregate_sum(self, samples: list[float]) -> float:
        return 0.0

    def aggregate_avg(self, samples: list[float]) -> float:
        return 0.0

    def aggregate_percentile(self, samples: list[float], p: float) -> float:
        return 0.0
