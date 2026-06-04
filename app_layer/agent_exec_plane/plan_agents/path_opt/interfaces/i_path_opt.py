from typing import Protocol, List, Dict, Any


class IPathOpt(Protocol):
    def analyze_path(self, path: List[str]) -> Dict[str, Any]:
        ...

    def optimize_path(self, path: List[str]) -> List[str]:
        ...

    def validate_path(self, path: List[str]) -> bool:
        ...

    def select_best_path(self, paths: List[List[str]]) -> List[str]:
        ...
