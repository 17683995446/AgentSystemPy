from typing import Protocol


class IGoalPriorityRank(Protocol):
    def score_goals(self) -> None:
        pass

    def rank_goals(self) -> None:
        pass

    def filter_goals(self) -> None:
        pass
