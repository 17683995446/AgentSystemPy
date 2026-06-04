from ..interfaces.i_global_plan import IGlobalPlan


class GlobalPlanImpl(IGlobalPlan):
    def create_plan(self, tasks: list[dict]) -> dict:
        plan = {"tasks": tasks, "status": "created"}
        return plan

    def merge_plans(self, plans: list[dict]) -> dict:
        merged = {"plans": plans, "status": "merged"}
        return merged

    def validate_plan(self, plan: dict) -> bool:
        valid = bool(plan.get("tasks"))
        return valid

    def execute_plan(self, plan: dict) -> dict:
        result = {"plan": plan, "status": "executed"}
        return result
