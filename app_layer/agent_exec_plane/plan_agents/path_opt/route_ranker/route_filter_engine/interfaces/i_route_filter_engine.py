from typing import Protocol


class IRouteFilterEngine(Protocol):
    def filter_by_cost(self, routes: list[dict], max_cost: float) -> list[dict]:
        ...

    def filter_by_risk(self, routes: list[dict], max_risk: float) -> list[dict]:
        ...

    def filter_by_time(self, routes: list[dict], max_time: float) -> list[dict]:
        ...
