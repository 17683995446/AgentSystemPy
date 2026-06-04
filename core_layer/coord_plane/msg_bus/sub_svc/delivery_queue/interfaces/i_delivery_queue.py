from typing import Protocol


class IDeliveryQueue(Protocol):
    def schedule_delivery(self) -> None:
        pass

    def retry_delivery(self) -> None:
        pass

    def ack_delivery(self) -> None:
        pass

    def purge_queue(self) -> None:
        pass
