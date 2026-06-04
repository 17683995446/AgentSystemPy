from typing import Protocol


class IConfRes(Protocol):
    def detect(self, rules: list[dict]) -> list[dict]:
        ...

    def resolve(self, conflicts: list[dict]) -> dict:
        ...

    def escalate(self, conflict: dict) -> bool:
        ...

    def log_conflict(self, conflict: dict) -> None:
        ...
