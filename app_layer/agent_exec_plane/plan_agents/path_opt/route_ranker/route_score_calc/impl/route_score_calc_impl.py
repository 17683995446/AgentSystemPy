from ..interfaces.i_route_score_calc import IRouteScoreCalc


class RouteScoreCalcImpl(IRouteScoreCalc):
    def calc_latency(self, route: dict) -> float:
        return 0.0

    def calc_reliability(self, route: dict) -> float:
        return 0.0

    def calc_cost(self, route: dict) -> float:
        return 0.0
