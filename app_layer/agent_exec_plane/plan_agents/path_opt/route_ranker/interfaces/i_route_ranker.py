from typing import Protocol


class IRouteRanker(Protocol):
    def score_routes(self) -> None:
        pass

    def rank_routes(self) -> None:
        pass

    def filter_top(self) -> None:
        pass

    def select_best(self) -> None:
        pass
