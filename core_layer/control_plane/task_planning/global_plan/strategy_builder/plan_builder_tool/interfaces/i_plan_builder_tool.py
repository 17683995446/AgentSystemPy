from typing import Protocol


class IPlanBuilderTool(Protocol):
    def define_tool(self) -> None:
        pass

    def build_tool(self) -> None:
        pass

    def validate_tool(self) -> None:
        pass
