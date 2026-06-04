from ..interfaces.i_output_template_mgr import IOutputTemplateMgr


class OutputTemplateMgrImpl(IOutputTemplateMgr):
    def load_template(self, name: str) -> str:
        return ""

    def render_template(self, template: str, context: dict) -> str:
        return ""

    def register_template(self, name: str, template: str) -> None:
        pass
