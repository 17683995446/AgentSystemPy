from ..interfaces.i_route_filter_engine import IRouteFilterEngine


class RouteFilterEngineImpl(IRouteFilterEngine):
    def filter_by_cost(self, routes: list[dict], max_cost: float) -> list[dict]:
        return []

    def filter_by_risk(self, routes: list[dict], max_risk: float) -> list[dict]:
        return []

    def filter_by_time(self, routes: list[dict], max_time: float) -> list[dict]:
        return []
