from typing import Protocol


class IVoteBallotBox(Protocol):
    def open_ballot(self) -> None:
        pass

    def cast_ballot(self) -> None:
        pass

    def close_ballot(self) -> None:
        pass
