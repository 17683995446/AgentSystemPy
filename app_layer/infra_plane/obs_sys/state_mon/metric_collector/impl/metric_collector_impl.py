from ..interfaces.i_metric_collector import IMetricCollector
class MetricCollectorImpl(IMetricCollector):
    def register_source(self) -> None:
        pass

    def collect_sample(self) -> None:
        pass

    def aggregate_data(self) -> None:
        pass

    def export_snapshot(self) -> None:
        pass
