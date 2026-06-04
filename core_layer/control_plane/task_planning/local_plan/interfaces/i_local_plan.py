from typing import Protocol


class ILocalPlan(Protocol):
    def create_local_plan(self, subtasks: list[dict]) -> dict:
        ...

    def merge_local_plans(self, plans: list[dict]) -> dict:
        ...

    def validate_local_plan(self, plan: dict) -> bool:
        ...

    def execute_local_plan(self, plan: dict) -> dict:
        ...
