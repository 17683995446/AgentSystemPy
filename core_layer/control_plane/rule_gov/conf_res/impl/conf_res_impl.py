from ..interfaces.i_conf_res import IConfRes


class ConfResImpl(IConfRes):
    def __init__(self) -> None:
        self._logs: list[dict] = []

    def detect(self, rules: list[dict]) -> list[dict]:
        conflicts = [r for r in rules if r.get("conflict", False)]
        return conflicts

    def resolve(self, conflicts: list[dict]) -> dict:
        result = {"resolved": len(conflicts), "conflicts": conflicts}
        return result

    def escalate(self, conflict: dict) -> bool:
        return conflict.get("severity", 0) > 5

    def log_conflict(self, conflict: dict) -> None:
        self._logs.append(conflict)
