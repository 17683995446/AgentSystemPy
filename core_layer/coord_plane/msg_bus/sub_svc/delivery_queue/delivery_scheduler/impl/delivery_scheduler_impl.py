from ..interfaces.i_delivery_scheduler import IDeliveryScheduler
class DeliverySchedulerImpl(IDeliveryScheduler):
    def schedule(self) -> None:
        pass

    def cancel(self) -> None:
        pass

    def reschedule(self) -> None:
        pass
