from typing import Protocol


class IPlanBuilderUnit(Protocol):
    def create_unit(self) -> None:
        pass

    def compose_unit(self) -> None:
        pass

    def test_unit(self) -> None:
        pass
