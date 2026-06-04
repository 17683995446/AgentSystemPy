from typing import Protocol


class ILogStreamPusher(Protocol):
    def connect_stream(self, url: str) -> object:
        ...

    def push_record(self, stream: object, record: dict) -> None:
        ...

    def disconnect_stream(self, stream: object) -> None:
        ...
