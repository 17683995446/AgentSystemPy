from typing import Protocol


class IRuleOverrideSet(Protocol):
    def add_override(self) -> None:
        pass

    def remove_override(self) -> None:
        pass

    def apply_override(self) -> None:
        pass
