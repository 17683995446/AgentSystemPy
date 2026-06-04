from ..interfaces.i_rule_arbiter import IRuleArbiter
class RuleArbiterImpl(IRuleArbiter):
    def load_rules(self) -> None:
        pass

    def prioritize(self) -> None:
        pass

    def override(self) -> None:
        pass

    def arbitrate(self) -> None:
        pass
