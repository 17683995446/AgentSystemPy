from typing import Protocol


class IStepDependencyGraph(Protocol):
    def add_node(self) -> None:
        pass

    def add_edge(self) -> None:
        pass

    def detect_cycle(self) -> None:
        pass
