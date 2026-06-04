from ..interfaces.i_vector_query_engine import IVectorQueryEngine


class VectorQueryEngineImpl(IVectorQueryEngine):
    def knn_search(self, query: list[float], k: int) -> list[dict]:
        return []

    def range_search(self, query: list[float], radius: float) -> list[dict]:
        return []

    def batch_query(self, queries: list[list[float]], k: int) -> list[list[dict]]:
        return []
