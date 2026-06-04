from ..interfaces.i_vote_tally_engine import IVoteTallyEngine
class VoteTallyEngineImpl(IVoteTallyEngine):
    def count_votes(self) -> None:
        pass

    def verify_quorum(self) -> None:
        pass

    def announce_result(self) -> None:
        pass
