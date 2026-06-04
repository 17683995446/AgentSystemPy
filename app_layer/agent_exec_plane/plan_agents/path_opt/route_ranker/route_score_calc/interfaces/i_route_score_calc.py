from typing import Protocol


class IRouteScoreCalc(Protocol):
    def calc_latency(self, route: dict) -> float:
        ...

    def calc_reliability(self, route: dict) -> float:
        ...

    def calc_cost(self, route: dict) -> float:
        ...
