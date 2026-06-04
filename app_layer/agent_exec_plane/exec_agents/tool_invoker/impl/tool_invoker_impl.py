from typing import List, Dict, Any
from ..interfaces.i_tool_invoker import IToolInvoker


class ToolInvokerImpl(IToolInvoker):
    def discover_tools(self) -> List[Dict[str, Any]]:
        return [{"name": "default"}]

    def invoke_tool(self, tool_name: str, params: Dict[str, Any]) -> Any:
        return {"tool": tool_name, "params": params}

    def handle_result(self, result: Any) -> Dict[str, Any]:
        return {"result": result, "ok": True}

    def retry_call(self, tool_name: str, params: Dict[str, Any], retries: int) -> Any:
        return self.invoke_tool(tool_name, params)
