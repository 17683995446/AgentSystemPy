from typing import Protocol


class IFilterRuleParser(Protocol):
    def parse_rule(self) -> None:
        pass

    def validate_rule(self) -> None:
        pass

    def compile_rule(self) -> None:
        pass
