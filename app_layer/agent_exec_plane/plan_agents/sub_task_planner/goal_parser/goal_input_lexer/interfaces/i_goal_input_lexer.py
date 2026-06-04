from typing import Protocol


class IGoalInputLexer(Protocol):
    def lex_input(self, raw_input: str) -> list[str]:
        ...

    def tokenize(self, lexed: list[str]) -> list[dict]:
        ...

    def classify_token(self, token: dict) -> str:
        ...
