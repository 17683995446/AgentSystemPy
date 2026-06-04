from typing import Protocol


class IRecallResultFilter(Protocol):
    def filter_by_threshold(self, results: list[dict], threshold: float) -> list[dict]:
        ...

    def filter_by_diversity(self, results: list[dict], k: int) -> list[dict]:
        ...

    def deduplicate(self, results: list[dict]) -> list[dict]:
        ...
