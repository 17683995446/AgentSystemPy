from ..interfaces.i_filter_engine import IFilterEngine
class FilterEngineImpl(IFilterEngine):
    def parse_rule(self) -> None:
        pass

    def match_msg(self) -> None:
        pass

    def apply_filter(self) -> None:
        pass

    def update_rule(self) -> None:
        pass
