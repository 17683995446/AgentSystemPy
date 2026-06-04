from typing import Protocol


class ITopicMetaStore(Protocol):
    def store_meta(self) -> None:
        pass

    def retrieve_meta(self) -> None:
        pass

    def delete_meta(self) -> None:
        pass
