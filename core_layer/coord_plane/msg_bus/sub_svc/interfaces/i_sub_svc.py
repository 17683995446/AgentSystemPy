from typing import Protocol


class ISubSvc(Protocol):
    def subscribe_topic(self, topic: str) -> bool:
        ...

    def unsubscribe_topic(self, topic: str) -> bool:
        ...

    def receive_msg(self) -> dict:
        ...

    def filter_msg(self, msgs: list[dict], criteria: dict) -> list[dict]:
        ...
