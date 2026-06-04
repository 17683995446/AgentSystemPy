from typing import Protocol, List, Dict, Any


class IToolInvoker(Protocol):
    def discover_tools(self) -> List[Dict[str, Any]]:
        ...

    def invoke_tool(self, tool_name: str, params: Dict[str, Any]) -> Any:
        ...

    def handle_result(self, result: Any) -> Dict[str, Any]:
        ...

    def retry_call(self, tool_name: str, params: Dict[str, Any], retries: int) -> Any:
        ...
