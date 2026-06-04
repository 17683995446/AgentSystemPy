from ..interfaces.i_tool_version_mgr import IToolVersionMgr


class ToolVersionMgrImpl(IToolVersionMgr):
    def register_version(self, tool_id: str, version: str) -> None:
        pass

    def deprecate_version(self, tool_id: str, version: str) -> None:
        pass

    def check_compat(self, version_a: str, version_b: str) -> bool:
        return True
