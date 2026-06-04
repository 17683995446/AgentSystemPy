from typing import Protocol


class ILoadDistributor(Protocol):
    def distribute(self) -> None:
        pass

    def rebalance(self) -> None:
        pass

    def drain_node(self) -> None:
        pass
