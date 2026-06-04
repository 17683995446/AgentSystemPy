from ..interfaces.i_vote_ballot_box import IVoteBallotBox
class VoteBallotBoxImpl(IVoteBallotBox):
    def open_ballot(self) -> None:
        pass

    def cast_ballot(self) -> None:
        pass

    def close_ballot(self) -> None:
        pass
