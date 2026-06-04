from typing import Protocol


class IDeliveryScheduler(Protocol):
    def schedule(self) -> None:
        pass

    def cancel(self) -> None:
        pass

    def reschedule(self) -> None:
        pass
