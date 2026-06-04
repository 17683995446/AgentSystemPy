from typing import Protocol


class IAccessAuditLog(Protocol):
    def log_access(self) -> None:
        pass

    def query_log(self) -> None:
        pass

    def export_log(self) -> None:
        pass
