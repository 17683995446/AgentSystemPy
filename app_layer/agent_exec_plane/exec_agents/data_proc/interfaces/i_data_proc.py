from typing import Protocol, Dict, Any


class IDataProc(Protocol):
    def parse_input(self, raw: str) -> Dict[str, Any]:
        ...

    def transform_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        ...

    def validate_data(self, data: Dict[str, Any]) -> bool:
        ...

    def output_result(self, data: Dict[str, Any]) -> str:
        ...
