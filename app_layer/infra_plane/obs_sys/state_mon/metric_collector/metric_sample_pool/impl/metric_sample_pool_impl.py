from ..interfaces.i_metric_sample_pool import IMetricSamplePool


class MetricSamplePoolImpl(IMetricSamplePool):
    def add_sample(self, metric_id: str, value: float) -> None:
        pass

    def evict_oldest(self, metric_id: str) -> None:
        pass

    def compute_stats(self, metric_id: str) -> dict:
        return {}
