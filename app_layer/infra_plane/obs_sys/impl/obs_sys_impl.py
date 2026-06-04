from app_layer.infra_plane.obs_sys.interfaces.i_obs_sys import IObsSys


class ObsSysImpl(IObsSys):
    def log_trace(self) -> None:
        pass

    def monitor_state(self) -> None:
        pass
