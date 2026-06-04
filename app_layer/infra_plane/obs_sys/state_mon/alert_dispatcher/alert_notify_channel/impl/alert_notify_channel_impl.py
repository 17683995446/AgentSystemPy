from ..interfaces.i_alert_notify_channel import IAlertNotifyChannel


class AlertNotifyChannelImpl(IAlertNotifyChannel):
    def send_email(self, to: str, subject: str, body: str) -> None:
        pass

    def send_webhook(self, url: str, payload: dict) -> None:
        pass

    def send_sms(self, phone: str, message: str) -> None:
        pass
