from typing import Protocol


class ITaskChunkMerger(Protocol):
    def merge_chunks(self, chunks: list[dict]) -> dict:
        ...

    def resolve_conflicts(self, merged: dict) -> dict:
        ...

    def validate_merge(self, merged: dict) -> bool:
        ...
