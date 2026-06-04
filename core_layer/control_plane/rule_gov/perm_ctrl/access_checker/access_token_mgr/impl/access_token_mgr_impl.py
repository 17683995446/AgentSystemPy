from ..interfaces.i_access_token_mgr import IAccessTokenMgr
class AccessTokenMgrImpl(IAccessTokenMgr):
    def issue_token(self) -> None:
        pass

    def refresh_token(self) -> None:
        pass

    def revoke_token(self) -> None:
        pass
