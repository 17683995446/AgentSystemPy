from typing import Protocol


class ISeqMgr(Protocol):
    def create_seq(self, items: list[dict]) -> dict:
        ...

    def reorder_seq(self, seq: dict, order: list[int]) -> dict:
        ...

    def validate_seq(self, seq: dict) -> bool:
        ...

    def execute_seq(self, seq: dict) -> dict:
        ...
