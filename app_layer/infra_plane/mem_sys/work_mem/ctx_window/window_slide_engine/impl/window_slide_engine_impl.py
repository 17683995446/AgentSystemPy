from ..interfaces.i_window_slide_engine import IWindowSlideEngine


class WindowSlideEngineImpl(IWindowSlideEngine):
    def slide_forward(self, window: dict, step: int) -> dict:
        return {}

    def slide_backward(self, window: dict, step: int) -> dict:
        return {}

    def recenter_window(self, window: dict, center: int) -> dict:
        return {}
