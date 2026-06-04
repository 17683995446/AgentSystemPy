from ..interfaces.i_step_rule_checker import IStepRuleChecker
class StepRuleCheckerImpl(IStepRuleChecker):
    def load_rules(self) -> None:
        pass

    def check_step(self) -> None:
        pass

    def report_violations(self) -> None:
        pass
