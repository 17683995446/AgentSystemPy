from typing import Protocol


class IGoalAnalyzer(Protocol):
    def parse_input(self) -> None:
        pass

    def decompose_tree(self) -> None:
        pass

    def analyze_priority(self) -> None:
        pass

    def validate_scope(self) -> None:
        pass
