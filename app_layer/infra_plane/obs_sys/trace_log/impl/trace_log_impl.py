from typing import List, Dict, Any
from ..interfaces.i_trace_log import ITraceLog


class TraceLogImpl(ITraceLog):
    def __init__(self) -> None:
        self._logs: List[Dict[str, Any]] = []

    def log_event(self, event: str, level: str) -> bool:
        self._logs.append({"event": event, "level": level})
        return True

    def query_log(self, level: str) -> List[str]:
        return [e["event"] for e in self._logs if e["level"] == level]

    def export_log(self, path: str) -> bool:
        return True

    def rotate_log(self) -> bool:
        self._logs.clear()
        return True
