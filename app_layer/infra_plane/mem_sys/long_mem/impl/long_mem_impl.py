from typing import List, Dict, Any, Optional
from ..interfaces.i_long_mem import ILongMem


class LongMemImpl(ILongMem):
    def __init__(self) -> None:
        self._store: dict[str, Dict[str, Any]] = {}

    def persist_mem(self, data: Dict[str, Any]) -> bool:
        mem_id = data.get("id", "")
        self._store[mem_id] = data
        return True

    def recall_mem(self, query: str) -> Optional[Dict[str, Any]]:
        return self._store.get(query)

    def forget_mem(self, mem_id: str) -> bool:
        self._store.pop(mem_id, None)
        return True

    def index_mem(self) -> List[str]:
        return list(self._store.keys())
