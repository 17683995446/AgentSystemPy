from ..interfaces.i_agent_match import IAgentMatch


class AgentMatchImpl(IAgentMatch):
    def match_agent(self, task: dict, agents: list[dict]) -> list[dict]:
        matched = [a for a in agents if task.get("skill") in a.get("skills", [])]
        return matched

    def score_agent(self, agent: dict, task: dict) -> float:
        score = 1.0 if task.get("skill") in agent.get("skills", []) else 0.0
        return score

    def select_agent(self, scores: list[tuple[dict, float]]) -> dict:
        best = max(scores, key=lambda x: x[1])[0] if scores else {}
        return best

    def bind_agent(self, task: dict, agent: dict) -> bool:
        task["agent_id"] = agent.get("id")
        return True
