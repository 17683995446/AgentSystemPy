from ..interfaces.i_task_chunk_merger import ITaskChunkMerger


class TaskChunkMergerImpl(ITaskChunkMerger):
    def merge_chunks(self, chunks: list[dict]) -> dict:
        return {}

    def resolve_conflicts(self, merged: dict) -> dict:
        return {}

    def validate_merge(self, merged: dict) -> bool:
        return True
