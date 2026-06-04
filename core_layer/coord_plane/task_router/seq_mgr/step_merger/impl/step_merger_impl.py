from ..interfaces.i_step_merger import IStepMerger
class StepMergerImpl(IStepMerger):
    def collect_batch(self) -> None:
        pass

    def merge_batch(self) -> None:
        pass

    def optimize_batch(self) -> None:
        pass

    def emit_batch(self) -> None:
        pass
