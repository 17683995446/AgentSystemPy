from typing import Protocol


class IStepParamBinder(Protocol):
    def bind_params(self) -> None:
        pass

    def validate_binding(self) -> None:
        pass

    def resolve_refs(self) -> None:
        pass
