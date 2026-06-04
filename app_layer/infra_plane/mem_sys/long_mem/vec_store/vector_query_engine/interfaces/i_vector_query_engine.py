from typing import Protocol


class IVectorQueryEngine(Protocol):
    def knn_search(self, query: list[float], k: int) -> list[dict]:
        ...

    def range_search(self, query: list[float], radius: float) -> list[dict]:
        ...

    def batch_query(self, queries: list[list[float]], k: int) -> list[list[dict]]:
        ...
