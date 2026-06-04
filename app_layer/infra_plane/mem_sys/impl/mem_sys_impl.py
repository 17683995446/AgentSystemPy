from app_layer.infra_plane.mem_sys.interfaces.i_mem_sys import IMemSys


class MemSysImpl(IMemSys):
    def persist(self) -> None:
        pass

    def recall(self) -> None:
        pass
