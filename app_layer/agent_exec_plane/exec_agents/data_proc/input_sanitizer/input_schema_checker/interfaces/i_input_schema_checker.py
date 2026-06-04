from typing import Protocol


class IInputSchemaChecker(Protocol):
    def load_schema(self, schema_path: str) -> dict:
        ...

    def validate_against_schema(self, data: dict, schema: dict) -> bool:
        ...

    def report_errors(self) -> list[str]:
        ...
