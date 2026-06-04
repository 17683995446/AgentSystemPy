from typing import Protocol


class ILogBatchCompressor(Protocol):
    def compress_batch(self, batch: list[dict]) -> bytes:
        ...

    def decompress_batch(self, data: bytes) -> list[dict]:
        ...

    def estimate_size(self, batch: list[dict]) -> int:
        ...
