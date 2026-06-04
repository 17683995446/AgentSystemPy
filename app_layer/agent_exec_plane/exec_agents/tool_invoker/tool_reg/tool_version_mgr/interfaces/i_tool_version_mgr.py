from typing import Protocol


class IToolVersionMgr(Protocol):
    def register_version(self, tool_id: str, version: str) -> None:
        ...

    def deprecate_version(self, tool_id: str, version: str) -> None:
        ...

    def check_compat(self, version_a: str, version_b: str) -> bool:
        ...
