from typing import Dict, Any, List
from ..interfaces.i_state_mon import IStateMon


class StateMonImpl(IStateMon):
    def collect_state(self) -> Dict[str, Any]:
        return {"status": "ok"}

    def analyze_state(self, state: Dict[str, Any]) -> Dict[str, Any]:
        return {"analyzed": True, "state": state}

    def alert_anomaly(self, anomaly: str) -> bool:
        return True

    def report_state(self) -> str:
        return "state_report"
