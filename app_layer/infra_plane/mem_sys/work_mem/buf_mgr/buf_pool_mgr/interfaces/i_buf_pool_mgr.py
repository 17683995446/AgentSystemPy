from typing import Protocol


class IBufPoolMgr(Protocol):
    def create_pool(self, size: int) -> object:
        ...

    def destroy_pool(self, pool: object) -> None:
        ...

    def resize_pool(self, pool: object, new_size: int) -> None:
        ...
