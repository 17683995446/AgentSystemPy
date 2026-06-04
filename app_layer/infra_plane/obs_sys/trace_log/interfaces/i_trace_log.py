from typing import Protocol, List, Dict, Any


class ITraceLog(Protocol):
    def log_event(self, event: str, level: str) -> bool:
        ...

    def query_log(self, level: str) -> List[str]:
        ...

    def export_log(self, path: str) -> bool:
        ...

    def rotate_log(self) -> bool:
        ...
