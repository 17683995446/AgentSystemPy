from typing import Protocol


class ILogBufferFlusher(Protocol):
    def flush_sync(self, buffer: list[dict]) -> None:
        ...

    def flush_async(self, buffer: list[dict]) -> None:
        ...

    def schedule_flush(self, interval_ms: int) -> None:
        ...
