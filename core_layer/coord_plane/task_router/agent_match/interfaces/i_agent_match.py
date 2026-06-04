from typing import Protocol


class IAgentMatch(Protocol):
    def match_agent(self, task: dict, agents: list[dict]) -> list[dict]:
        ...

    def score_agent(self, agent: dict, task: dict) -> float:
        ...

    def select_agent(self, scores: list[tuple[dict, float]]) -> dict:
        ...

    def bind_agent(self, task: dict, agent: dict) -> bool:
        ...
