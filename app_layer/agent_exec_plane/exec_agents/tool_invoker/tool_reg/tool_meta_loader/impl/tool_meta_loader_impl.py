from ..interfaces.i_tool_meta_loader import IToolMetaLoader


class ToolMetaLoaderImpl(IToolMetaLoader):
    def load_meta(self, tool_id: str) -> dict:
        return {}

    def validate_meta(self, meta: dict) -> bool:
        return True

    def cache_meta(self, tool_id: str, meta: dict) -> None:
        pass
