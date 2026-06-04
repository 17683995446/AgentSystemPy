from ..interfaces.i_buf_pool_mgr import IBufPoolMgr


class BufPoolMgrImpl(IBufPoolMgr):
    def create_pool(self, size: int) -> object:
        return object()

    def destroy_pool(self, pool: object) -> None:
        pass

    def resize_pool(self, pool: object, new_size: int) -> None:
        pass
