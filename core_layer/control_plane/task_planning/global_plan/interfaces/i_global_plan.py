from typing import Protocol


class IGlobalPlan(Protocol):
    def create_plan(self, tasks: list[dict]) -> dict:
        ...

    def merge_plans(self, plans: list[dict]) -> dict:
        ...

    def validate_plan(self, plan: dict) -> bool:
        ...

    def execute_plan(self, plan: dict) -> dict:
        ...
