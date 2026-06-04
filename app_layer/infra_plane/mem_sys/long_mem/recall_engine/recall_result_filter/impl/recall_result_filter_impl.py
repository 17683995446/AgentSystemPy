from ..interfaces.i_recall_result_filter import IRecallResultFilter


class RecallResultFilterImpl(IRecallResultFilter):
    def filter_by_threshold(self, results: list[dict], threshold: float) -> list[dict]:
        return []

    def filter_by_diversity(self, results: list[dict], k: int) -> list[dict]:
        return []

    def deduplicate(self, results: list[dict]) -> list[dict]:
        return []
