from typing import Protocol


class IRoleMgr(Protocol):
    def create_role(self) -> None:
        pass

    def edit_role(self) -> None:
        pass

    def assign_role(self) -> None:
        pass

    def revoke_role(self) -> None:
        pass
