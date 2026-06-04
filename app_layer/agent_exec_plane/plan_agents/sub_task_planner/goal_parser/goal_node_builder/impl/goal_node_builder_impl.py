from ..interfaces.i_goal_node_builder import IGoalNodeBuilder


class GoalNodeBuilderImpl(IGoalNodeBuilder):
    def create_node(self, label: str) -> dict:
        return {}

    def link_nodes(self, parent: dict, child: dict) -> None:
        pass

    def validate_tree(self, root: dict) -> bool:
        return True
