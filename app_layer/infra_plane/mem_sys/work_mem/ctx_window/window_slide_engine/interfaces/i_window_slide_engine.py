from typing import Protocol


class IWindowSlideEngine(Protocol):
    def slide_forward(self, window: dict, step: int) -> dict:
        ...

    def slide_backward(self, window: dict, step: int) -> dict:
        ...

    def recenter_window(self, window: dict, center: int) -> dict:
        ...
