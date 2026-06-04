from typing import Protocol


class IAlertNotifyChannel(Protocol):
    def send_email(self, to: str, subject: str, body: str) -> None:
        ...

    def send_webhook(self, url: str, payload: dict) -> None:
        ...

    def send_sms(self, phone: str, message: str) -> None:
        ...
