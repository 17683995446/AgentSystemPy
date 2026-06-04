from ..interfaces.i_alert_dispatcher import IAlertDispatcher
class AlertDispatcherImpl(IAlertDispatcher):
    def register_rule(self) -> None:
        pass

    def evaluate_condition(self) -> None:
        pass

    def dispatch_alert(self) -> None:
        pass

    def resolve_alert(self) -> None:
        pass
