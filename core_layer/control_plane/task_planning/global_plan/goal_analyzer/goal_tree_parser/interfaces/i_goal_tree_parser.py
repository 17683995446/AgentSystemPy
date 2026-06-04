from typing import Protocol


class IGoalTreeParser(Protocol):
    def tokenize(self) -> None:
        pass

    def parse_nodes(self) -> None:
        pass

    def build_tree(self) -> None:
        pass
