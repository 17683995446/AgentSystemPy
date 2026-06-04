from typing import Protocol


class ICtxWindow(Protocol):
    def open_window(self) -> None:
        pass

    def close_window(self) -> None:
        pass

    def shift_window(self) -> None:
        pass

    def trim_window(self) -> None:
        pass
