from ..interfaces.i_log_buffer_flusher import ILogBufferFlusher


class LogBufferFlusherImpl(ILogBufferFlusher):
    def flush_sync(self, buffer: list[dict]) -> None:
        pass

    def flush_async(self, buffer: list[dict]) -> None:
        pass

    def schedule_flush(self, interval_ms: int) -> None:
        pass
