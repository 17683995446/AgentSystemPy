from typing import Protocol


class IResultTypeMapper(Protocol):
    def map_type(self, raw_value: object, target_type: type) -> object:
        ...

    def coerce_type(self, value: object, target_type: type) -> object:
        ...

    def validate_type(self, value: object, expected_type: type) -> bool:
        ...
