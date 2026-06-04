from typing import Protocol


class IOutputTemplateMgr(Protocol):
    def load_template(self, name: str) -> str:
        ...

    def render_template(self, template: str, context: dict) -> str:
        ...

    def register_template(self, name: str, template: str) -> None:
        ...
