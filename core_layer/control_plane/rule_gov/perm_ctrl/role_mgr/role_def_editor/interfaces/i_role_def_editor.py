from typing import Protocol


class IRoleDefEditor(Protocol):
    def create_def(self) -> None:
        pass

    def edit_def(self) -> None:
        pass

    def delete_def(self) -> None:
        pass
