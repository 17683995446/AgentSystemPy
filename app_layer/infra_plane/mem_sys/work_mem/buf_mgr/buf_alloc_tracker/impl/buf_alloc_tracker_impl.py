from ..interfaces.i_buf_alloc_tracker import IBufAllocTracker


class BufAllocTrackerImpl(IBufAllocTracker):
    def track_alloc(self, buf_id: str, size: int) -> None:
        pass

    def track_free(self, buf_id: str) -> None:
        pass

    def report_usage(self) -> dict:
        return {}
