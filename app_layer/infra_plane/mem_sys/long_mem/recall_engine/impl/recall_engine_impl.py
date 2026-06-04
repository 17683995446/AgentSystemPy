from ..interfaces.i_recall_engine import IRecallEngine
class RecallEngineImpl(IRecallEngine):
    def search_index(self) -> None:
        pass

    def rank_results(self) -> None:
        pass

    def filter_results(self) -> None:
        pass

    def return_top(self) -> None:
        pass
