from ..interfaces.i_access_audit_log import IAccessAuditLog
class AccessAuditLogImpl(IAccessAuditLog):
    def log_access(self) -> None:
        pass

    def query_log(self) -> None:
        pass

    def export_log(self) -> None:
        pass
