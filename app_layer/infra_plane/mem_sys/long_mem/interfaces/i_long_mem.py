from typing import Protocol, List, Dict, Any, Optional


class ILongMem(Protocol):
    def persist_mem(self, data: Dict[str, Any]) -> bool:
        ...

    def recall_mem(self, query: str) -> Optional[Dict[str, Any]]:
        ...

    def forget_mem(self, mem_id: str) -> bool:
        ...

    def index_mem(self) -> List[str]:
        ...
