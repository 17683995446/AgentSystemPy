from typing import Protocol, Dict, Any, Optional


class IWorkMem(Protocol):
    def store_ctx(self, key: str, value: Any) -> bool:
        ...

    def retrieve_ctx(self, key: str) -> Optional[Any]:
        ...

    def clear_ctx(self, key: str) -> bool:
        ...

    def update_ctx(self, key: str, value: Any) -> bool:
        ...
