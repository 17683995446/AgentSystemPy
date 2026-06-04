from ..interfaces.i_step_safety_guard import IStepSafetyGuard
class StepSafetyGuardImpl(IStepSafetyGuard):
    def scan_risks(self) -> None:
        pass

    def enforce_limits(self) -> None:
        pass

    def abort_if_unsafe(self) -> None:
        pass
