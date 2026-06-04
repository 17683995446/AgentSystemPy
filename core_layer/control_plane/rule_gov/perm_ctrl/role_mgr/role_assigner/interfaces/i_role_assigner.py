from typing import Protocol


class IRoleAssigner(Protocol):
    def assign_role(self) -> None:
        pass

    def revoke_role(self) -> None:
        pass

    def list_assignments(self) -> None:
        pass
