from typing import Protocol


class ILogAggregator(Protocol):
    def collect_batch(self) -> None:
        pass

    def aggregate_data(self) -> None:
        pass

    def compress_batch(self) -> None:
        pass

    def flush_buffer(self) -> None:
        pass
