from typing import Protocol


class IDeliveryRetryMgr(Protocol):
    def schedule_retry(self) -> None:
        pass

    def backoff(self) -> None:
        pass

    def give_up(self) -> None:
        pass
