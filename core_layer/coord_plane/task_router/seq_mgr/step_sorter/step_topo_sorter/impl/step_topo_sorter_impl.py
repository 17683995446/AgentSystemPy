from ..interfaces.i_step_topo_sorter import IStepTopoSorter
class StepTopoSorterImpl(IStepTopoSorter):
    def sort(self) -> None:
        pass

    def validate_order(self) -> None:
        pass

    def handle_cycle(self) -> None:
        pass
