from typing import Protocol


class IVoteTallyEngine(Protocol):
    def count_votes(self) -> None:
        pass

    def verify_quorum(self) -> None:
        pass

    def announce_result(self) -> None:
        pass
