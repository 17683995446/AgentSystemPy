from ..interfaces.i_log_stream_pusher import ILogStreamPusher


class LogStreamPusherImpl(ILogStreamPusher):
    def connect_stream(self, url: str) -> object:
        return object()

    def push_record(self, stream: object, record: dict) -> None:
        pass

    def disconnect_stream(self, stream: object) -> None:
        pass
