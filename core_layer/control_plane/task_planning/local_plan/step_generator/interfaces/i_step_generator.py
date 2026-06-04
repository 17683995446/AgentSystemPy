from typing import Protocol


class IStepGenerator(Protocol):
    def generate_step(self) -> None:
        pass

    def bind_params(self) -> None:
        pass

    def validate_step(self) -> None:
        pass

    def emit_step(self) -> None:
        pass
