from ..interfaces.i_load_metric_collector import ILoadMetricCollector
class LoadMetricCollectorImpl(ILoadMetricCollector):
    def collect_cpu(self) -> None:
        pass

    def collect_mem(self) -> None:
        pass

    def collect_queue(self) -> None:
        pass
