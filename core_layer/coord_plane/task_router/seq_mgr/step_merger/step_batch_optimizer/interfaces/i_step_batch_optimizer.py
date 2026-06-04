from typing import Protocol


class IStepBatchOptimizer(Protocol):
    def optimize(self) -> None:
        pass

    def merge_similar(self) -> None:
        pass

    def deduplicate(self) -> None:
        pass
