from typing import Protocol


class ISkillTagIndexer(Protocol):
    def index_tag(self) -> None:
        pass

    def search_tag(self) -> None:
        pass

    def remove_tag(self) -> None:
        pass
