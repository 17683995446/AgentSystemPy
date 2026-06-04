from typing import Protocol, List, Dict, Any


class ISubTaskPlanner(Protocol):
    def decompose_goal(self, goal: str) -> List[Dict[str, Any]]:
        ...

    def assign_subtask(self, subtask: Dict[str, Any], agent_id: str) -> bool:
        ...

    def track_subtask(self, subtask_id: str) -> Dict[str, Any]:
        ...

    def merge_subtasks(self, subtasks: List[Dict[str, Any]]) -> Dict[str, Any]:
        ...
