from typing import Protocol


class IStepTemplateLib(Protocol):
    def load_template(self) -> None:
        pass

    def save_template(self) -> None:
        pass

    def list_templates(self) -> None:
        pass
