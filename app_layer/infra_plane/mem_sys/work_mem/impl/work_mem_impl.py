from typing import Any, Optional
from ..interfaces.i_work_mem import IWorkMem


class WorkMemImpl(IWorkMem):
    def __init__(self) -> None:
        self._mem: dict[str, Any] = {}

    def store_ctx(self, key: str, value: Any) -> bool:
        self._mem[key] = value
        return True

    def retrieve_ctx(self, key: str) -> Optional[Any]:
        return self._mem.get(key)

    def clear_ctx(self, key: str) -> bool:
        self._mem.pop(key, None)
        return True

    def update_ctx(self, key: str, value: Any) -> bool:
        self._mem[key] = value
        return True
