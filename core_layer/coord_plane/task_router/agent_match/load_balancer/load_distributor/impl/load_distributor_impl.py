from ..interfaces.i_load_distributor import ILoadDistributor
class LoadDistributorImpl(ILoadDistributor):
    def distribute(self) -> None:
        pass

    def rebalance(self) -> None:
        pass

    def drain_node(self) -> None:
        pass
