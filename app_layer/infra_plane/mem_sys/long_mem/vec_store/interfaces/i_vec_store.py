from typing import Protocol


class IVecStore(Protocol):
    def store_vec(self) -> None:
        pass

    def query_vec(self) -> None:
        pass

    def delete_vec(self) -> None:
        pass

    def index_vec(self) -> None:
        pass
