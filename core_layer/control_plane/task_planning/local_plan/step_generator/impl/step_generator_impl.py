from ..interfaces.i_step_generator import IStepGenerator
class StepGeneratorImpl(IStepGenerator):
    def generate_step(self) -> None:
        pass

    def bind_params(self) -> None:
        pass

    def validate_step(self) -> None:
        pass

    def emit_step(self) -> None:
        pass
