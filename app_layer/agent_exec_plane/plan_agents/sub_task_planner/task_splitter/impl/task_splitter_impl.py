from ..interfaces.i_task_splitter import ITaskSplitter
class TaskSplitterImpl(ITaskSplitter):
    def estimate_size(self) -> None:
        pass

    def split_by_rule(self) -> None:
        pass

    def assign_ids(self) -> None:
        pass

    def link_chunks(self) -> None:
        pass
