from typing import Protocol


class ICostEstimator(Protocol):
    def estimate_time(self) -> None:
        pass

    def estimate_resource(self) -> None:
        pass

    def estimate_risk(self) -> None:
        pass

    def sum_total(self) -> None:
        pass
