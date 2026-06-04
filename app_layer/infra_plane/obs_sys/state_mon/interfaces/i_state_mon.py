from typing import Protocol, Dict, Any, List


class IStateMon(Protocol):
    def collect_state(self) -> Dict[str, Any]:
        ...

    def analyze_state(self, state: Dict[str, Any]) -> Dict[str, Any]:
        ...

    def alert_anomaly(self, anomaly: str) -> bool:
        ...

    def report_state(self) -> str:
        ...
