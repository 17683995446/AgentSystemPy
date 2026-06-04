from typing import Protocol


class IVectorIndexBuilder(Protocol):
    def build_index(self, vectors: list[list[float]]) -> object:
        ...

    def update_index(self, index: object, vectors: list[list[float]]) -> None:
        ...

    def optimize_index(self, index: object) -> None:
        ...
