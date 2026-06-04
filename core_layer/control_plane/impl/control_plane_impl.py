from core_layer.control_plane.interfaces.i_control_plane import IControlPlane


class ControlPlaneImpl(IControlPlane):
    def plan_task(self) -> None:
        pass

    def govern_rules(self) -> None:
        pass
