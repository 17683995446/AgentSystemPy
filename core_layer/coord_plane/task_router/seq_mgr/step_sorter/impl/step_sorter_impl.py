from ..interfaces.i_step_sorter import IStepSorter
class StepSorterImpl(IStepSorter):
    def build_graph(self) -> None:
        pass

    def topo_sort(self) -> None:
        pass

    def detect_cycles(self) -> None:
        pass

    def reorder_steps(self) -> None:
        pass
