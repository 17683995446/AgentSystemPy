from ..interfaces.i_alert_rule_engine import IAlertRuleEngine


class AlertRuleEngineImpl(IAlertRuleEngine):
    def load_rules(self, rules_path: str) -> list[dict]:
        return []

    def evaluate_rules(self, state: dict, rules: list[dict]) -> list[dict]:
        return []

    def match_conditions(self, state: dict, conditions: list[dict]) -> bool:
        return True
