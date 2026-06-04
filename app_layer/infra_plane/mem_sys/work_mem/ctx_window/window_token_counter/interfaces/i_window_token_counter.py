from typing import Protocol


class IWindowTokenCounter(Protocol):
    def count_tokens(self, text: str) -> int:
        ...

    def estimate_tokens(self, text: str) -> int:
        ...

    def truncate_to_limit(self, text: str, limit: int) -> str:
        ...
