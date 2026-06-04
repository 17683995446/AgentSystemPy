from typing import Protocol


class ISkillSearchEngine(Protocol):
    def search(self) -> None:
        pass

    def rank_results(self) -> None:
        pass

    def filter_results(self) -> None:
        pass
