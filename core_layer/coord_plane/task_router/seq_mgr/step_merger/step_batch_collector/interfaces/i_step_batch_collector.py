from typing import Protocol


class IStepBatchCollector(Protocol):
    def collect(self) -> None:
        pass

    def group(self) -> None:
        pass

    def sort_batch(self) -> None:
        pass
