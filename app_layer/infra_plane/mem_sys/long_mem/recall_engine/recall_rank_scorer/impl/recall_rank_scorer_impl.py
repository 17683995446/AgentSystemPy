from ..interfaces.i_recall_rank_scorer import IRecallRankScorer


class RecallRankScorerImpl(IRecallRankScorer):
    def score_relevance(self, query: str, result: dict) -> float:
        return 0.0

    def score_recency(self, result: dict) -> float:
        return 0.0

    def score_frequency(self, result: dict) -> float:
        return 0.0
