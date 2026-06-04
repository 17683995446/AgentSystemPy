from ..interfaces.i_time_cost_model import ITimeCostModel


class TimeCostModelImpl(ITimeCostModel):
    def estimate_latency(self, path: dict) -> float:
        return 0.0

    def estimate_duration(self, path: dict) -> float:
        return 0.0

    def estimate_deadline(self, path: dict) -> float:
        return 0.0
