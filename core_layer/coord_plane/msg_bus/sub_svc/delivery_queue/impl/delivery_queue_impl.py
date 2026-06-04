from ..interfaces.i_delivery_queue import IDeliveryQueue
class DeliveryQueueImpl(IDeliveryQueue):
    def schedule_delivery(self) -> None:
        pass

    def retry_delivery(self) -> None:
        pass

    def ack_delivery(self) -> None:
        pass

    def purge_queue(self) -> None:
        pass
