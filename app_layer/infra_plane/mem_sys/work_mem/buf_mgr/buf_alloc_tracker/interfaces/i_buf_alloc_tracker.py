from typing import Protocol


class IBufAllocTracker(Protocol):
    def track_alloc(self, buf_id: str, size: int) -> None:
        ...

    def track_free(self, buf_id: str) -> None:
        ...

    def report_usage(self) -> dict:
        ...
