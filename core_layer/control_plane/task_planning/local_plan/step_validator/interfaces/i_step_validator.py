from typing import Protocol


class IStepValidator(Protocol):
    def check_rules(self) -> None:
        pass

    def check_safety(self) -> None:
        pass

    def check_deps(self) -> None:
        pass

    def report_errors(self) -> None:
        pass
