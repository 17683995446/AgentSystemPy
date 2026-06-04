from typing import Protocol


class IFilterMatcher(Protocol):
    def match_msg(self) -> None:
        pass

    def score_match(self) -> None:
        pass

    def batch_match(self) -> None:
        pass
