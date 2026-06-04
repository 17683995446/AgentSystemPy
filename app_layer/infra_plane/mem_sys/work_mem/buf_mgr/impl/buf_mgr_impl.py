from ..interfaces.i_buf_mgr import IBufMgr
class BufMgrImpl(IBufMgr):
    def alloc_buf(self) -> None:
        pass

    def release_buf(self) -> None:
        pass

    def defrag_buf(self) -> None:
        pass

    def resize_buf(self) -> None:
        pass
