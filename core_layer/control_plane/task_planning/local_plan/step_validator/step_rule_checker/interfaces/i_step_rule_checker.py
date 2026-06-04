from typing import Protocol


class IStepRuleChecker(Protocol):
    def load_rules(self) -> None:
        pass

    def check_step(self) -> None:
        pass

    def report_violations(self) -> None:
        pass
