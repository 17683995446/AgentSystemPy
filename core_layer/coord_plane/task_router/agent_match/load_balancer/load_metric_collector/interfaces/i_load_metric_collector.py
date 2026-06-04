from typing import Protocol


class ILoadMetricCollector(Protocol):
    def collect_cpu(self) -> None:
        pass

    def collect_mem(self) -> None:
        pass

    def collect_queue(self) -> None:
        pass
