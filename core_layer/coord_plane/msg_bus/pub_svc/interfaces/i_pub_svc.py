from typing import Protocol


class IPubSvc(Protocol):
    def publish_msg(self, topic: str, msg: dict) -> bool:
        ...

    def broadcast_msg(self, msg: dict) -> bool:
        ...

    def validate_msg(self, msg: dict) -> bool:
        ...

    def route_msg(self, msg: dict, target: str) -> bool:
        ...
