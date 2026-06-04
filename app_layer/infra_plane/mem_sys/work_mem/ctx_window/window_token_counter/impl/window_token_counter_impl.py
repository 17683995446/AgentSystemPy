from ..interfaces.i_window_token_counter import IWindowTokenCounter


class WindowTokenCounterImpl(IWindowTokenCounter):
    def count_tokens(self, text: str) -> int:
        return 0

    def estimate_tokens(self, text: str) -> int:
        return 0

    def truncate_to_limit(self, text: str, limit: int) -> str:
        return text
