from typing import Protocol


class IRecallRankScorer(Protocol):
    def score_relevance(self, query: str, result: dict) -> float:
        ...

    def score_recency(self, result: dict) -> float:
        ...

    def score_frequency(self, result: dict) -> float:
        ...
