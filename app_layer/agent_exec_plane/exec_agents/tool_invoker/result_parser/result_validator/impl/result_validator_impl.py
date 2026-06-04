from ..interfaces.i_result_validator import IResultValidator


class ResultValidatorImpl(IResultValidator):
    def validate_schema(self, result: dict, schema: dict) -> bool:
        return True

    def validate_range(self, value: float, min_val: float, max_val: float) -> bool:
        return True

    def validate_format(self, data: str, fmt: str) -> bool:
        return True
