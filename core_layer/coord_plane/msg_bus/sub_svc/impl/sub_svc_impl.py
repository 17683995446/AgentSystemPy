from ..interfaces.i_sub_svc import ISubSvc


class SubSvcImpl(ISubSvc):
    def __init__(self) -> None:
        self._subs: list[str] = []
        self._inbox: list[dict] = []

    def subscribe_topic(self, topic: str) -> bool:
        self._subs.append(topic)
        return True

    def unsubscribe_topic(self, topic: str) -> bool:
        self._subs = [t for t in self._subs if t != topic]
        return True

    def receive_msg(self) -> dict:
        return self._inbox.pop(0) if self._inbox else {}

    def filter_msg(self, msgs: list[dict], criteria: dict) -> list[dict]:
        filtered = [m for m in msgs if all(m.get(k) == v for k, v in criteria.items())]
        return filtered
