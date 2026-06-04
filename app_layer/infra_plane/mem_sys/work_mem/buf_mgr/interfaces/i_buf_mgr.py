from typing import Protocol


class IBufMgr(Protocol):
    def alloc_buf(self) -> None:
        pass

    def release_buf(self) -> None:
        pass

    def defrag_buf(self) -> None:
        pass

    def resize_buf(self) -> None:
        pass
