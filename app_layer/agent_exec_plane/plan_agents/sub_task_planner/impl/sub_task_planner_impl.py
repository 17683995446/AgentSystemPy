from typing import List, Dict, Any
from ..interfaces.i_sub_task_planner import ISubTaskPlanner


class SubTaskPlannerImpl(ISubTaskPlanner):
    def decompose_goal(self, goal: str) -> List[Dict[str, Any]]:
        return [{"goal": goal, "steps": []}]

    def assign_subtask(self, subtask: Dict[str, Any], agent_id: str) -> bool:
        subtask["agent"] = agent_id
        return True

    def track_subtask(self, subtask_id: str) -> Dict[str, Any]:
        return {"id": subtask_id, "status": "running"}

    def merge_subtasks(self, subtasks: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {"merged": True, "count": len(subtasks)}
