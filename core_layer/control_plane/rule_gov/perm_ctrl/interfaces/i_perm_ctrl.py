from typing import Protocol


class IPermCtrl(Protocol):
    def grant(self, subject: str, resource: str, action: str) -> bool:
        ...

    def revoke(self, subject: str, resource: str, action: str) -> bool:
        ...

    def check(self, subject: str, resource: str, action: str) -> bool:
        ...

    def list_perms(self, subject: str) -> list[dict]:
        ...
