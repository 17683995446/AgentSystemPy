from typing import Protocol


class IAlertRuleEngine(Protocol):
    def load_rules(self, rules_path: str) -> list[dict]:
        ...

    def evaluate_rules(self, state: dict, rules: list[dict]) -> list[dict]:
        ...

    def match_conditions(self, state: dict, conditions: list[dict]) -> bool:
        ...
