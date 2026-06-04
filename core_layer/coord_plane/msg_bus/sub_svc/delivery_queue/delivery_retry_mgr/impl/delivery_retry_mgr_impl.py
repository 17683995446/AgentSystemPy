from ..interfaces.i_delivery_retry_mgr import IDeliveryRetryMgr
class DeliveryRetryMgrImpl(IDeliveryRetryMgr):
    def schedule_retry(self) -> None:
        pass

    def backoff(self) -> None:
        pass

    def give_up(self) -> None:
        pass
