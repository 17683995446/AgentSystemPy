from typing import Protocol


class IStepSafetyGuard(Protocol):
    def scan_risks(self) -> None:
        pass

    def enforce_limits(self) -> None:
        pass

    def abort_if_unsafe(self) -> None:
        pass
