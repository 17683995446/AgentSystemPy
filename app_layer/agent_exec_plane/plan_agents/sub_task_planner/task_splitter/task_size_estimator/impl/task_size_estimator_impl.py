from ..interfaces.i_task_size_estimator import ITaskSizeEstimator


class TaskSizeEstimatorImpl(ITaskSizeEstimator):
    def estimate_complexity(self, task: dict) -> int:
        return 0

    def estimate_time(self, task: dict) -> float:
        return 0.0

    def estimate_memory(self, task: dict) -> int:
        return 0
