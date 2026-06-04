from typing import Protocol


class ILoadBalancer(Protocol):
    def collect_metrics(self) -> None:
        pass

    def distribute_load(self) -> None:
        pass

    def rebalance(self) -> None:
        pass

    def report_status(self) -> None:
        pass
