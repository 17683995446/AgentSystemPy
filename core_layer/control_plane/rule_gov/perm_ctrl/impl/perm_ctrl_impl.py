from ..interfaces.i_perm_ctrl import IPermCtrl


class PermCtrlImpl(IPermCtrl):
    def __init__(self) -> None:
        self._perms: list[dict] = []

    def grant(self, subject: str, resource: str, action: str) -> bool:
        self._perms.append({"subject": subject, "resource": resource, "action": action})
        return True

    def revoke(self, subject: str, resource: str, action: str) -> bool:
        self._perms = [p for p in self._perms if not (p["subject"] == subject and p["resource"] == resource and p["action"] == action)]
        return True

    def check(self, subject: str, resource: str, action: str) -> bool:
        found = any(p["subject"] == subject and p["resource"] == resource and p["action"] == action for p in self._perms)
        return found

    def list_perms(self, subject: str) -> list[dict]:
        perms = [p for p in self._perms if p["subject"] == subject]
        return perms
