from ..interfaces.i_local_plan import ILocalPlan


class LocalPlanImpl(ILocalPlan):
    def create_local_plan(self, subtasks: list[dict]) -> dict:
        plan = {"subtasks": subtasks, "status": "created"}
        return plan

    def merge_local_plans(self, plans: list[dict]) -> dict:
        merged = {"plans": plans, "status": "merged"}
        return merged

    def validate_local_plan(self, plan: dict) -> bool:
        valid = bool(plan.get("subtasks"))
        return valid

    def execute_local_plan(self, plan: dict) -> dict:
        result = {"plan": plan, "status": "executed"}
        return result
