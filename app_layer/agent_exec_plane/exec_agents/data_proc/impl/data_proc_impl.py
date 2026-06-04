from typing import Dict, Any
from ..interfaces.i_data_proc import IDataProc


class DataProcImpl(IDataProc):
    def parse_input(self, raw: str) -> Dict[str, Any]:
        return {"raw": raw}

    def transform_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        data["transformed"] = True
        return data

    def validate_data(self, data: Dict[str, Any]) -> bool:
        return isinstance(data, dict)

    def output_result(self, data: Dict[str, Any]) -> str:
        return str(data)
