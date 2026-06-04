from typing import Protocol


class IStepTopoSorter(Protocol):
    def sort(self) -> None:
        pass

    def validate_order(self) -> None:
        pass

    def handle_cycle(self) -> None:
        pass
