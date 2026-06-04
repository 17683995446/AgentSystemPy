from typing import Protocol


class IGoalNodeBuilder(Protocol):
    def create_node(self, label: str) -> dict:
        ...

    def link_nodes(self, parent: dict, child: dict) -> None:
        ...

    def validate_tree(self, root: dict) -> bool:
        ...
