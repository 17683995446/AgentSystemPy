from typing import Protocol


class IGoalParser(Protocol):
    def lex_input(self) -> None:
        pass

    def parse_tree(self) -> None:
        pass

    def extract_params(self) -> None:
        pass

    def validate_syntax(self) -> None:
        pass
