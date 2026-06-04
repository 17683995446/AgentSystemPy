from ..interfaces.i_vote_collector import IVoteCollector
class VoteCollectorImpl(IVoteCollector):
    def open_ballot(self) -> None:
        pass

    def cast_vote(self) -> None:
        pass

    def tally_votes(self) -> None:
        pass

    def announce_result(self) -> None:
        pass
