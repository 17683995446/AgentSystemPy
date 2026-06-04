from typing import Protocol


class IResultValidator(Protocol):
    def validate_schema(self, result: dict, schema: dict) -> bool:
        ...

    def validate_range(self, value: float, min_val: float, max_val: float) -> bool:
        ...

    def validate_format(self, data: str, fmt: str) -> bool:
        ...
