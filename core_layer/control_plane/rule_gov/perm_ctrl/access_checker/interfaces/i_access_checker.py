from typing import Protocol


class IAccessChecker(Protocol):
    def issue_token(self) -> None:
        pass

    def verify_token(self) -> None:
        pass

    def audit_access(self) -> None:
        pass

    def log_access(self) -> None:
        pass
