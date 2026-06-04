from typing import Protocol


class IToolMetaLoader(Protocol):
    def load_meta(self, tool_id: str) -> dict:
        ...

    def validate_meta(self, meta: dict) -> bool:
        ...

    def cache_meta(self, tool_id: str, meta: dict) -> None:
        ...
