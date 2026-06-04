from ..interfaces.i_input_schema_checker import IInputSchemaChecker


class InputSchemaCheckerImpl(IInputSchemaChecker):
    def load_schema(self, schema_path: str) -> dict:
        return {}

    def validate_against_schema(self, data: dict, schema: dict) -> bool:
        return True

    def report_errors(self) -> list[str]:
        return []
