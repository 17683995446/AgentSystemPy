from typing import Protocol


class IInputNormalizer(Protocol):
    def normalize_whitespace(self, text: str) -> str:
        ...

    def normalize_case(self, text: str, lower: bool = True) -> str:
        ...

    def normalize_encoding(self, text: str, encoding: str = "utf-8") -> str:
        ...
