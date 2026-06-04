from ..interfaces.i_rule_gov import IRuleGov


class RuleGovImpl(IRuleGov):
    def enforce_policy(self) -> None:
        pass

    def audit_compliance(self) -> None:
        pass
