from ..interfaces.i_vector_index_builder import IVectorIndexBuilder


class VectorIndexBuilderImpl(IVectorIndexBuilder):
    def build_index(self, vectors: list[list[float]]) -> object:
        return object()

    def update_index(self, index: object, vectors: list[list[float]]) -> None:
        pass

    def optimize_index(self, index: object) -> None:
        pass
