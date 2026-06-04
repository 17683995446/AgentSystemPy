from ..interfaces.i_log_batch_compressor import ILogBatchCompressor


class LogBatchCompressorImpl(ILogBatchCompressor):
    def compress_batch(self, batch: list[dict]) -> bytes:
        return b""

    def decompress_batch(self, data: bytes) -> list[dict]:
        return []

    def estimate_size(self, batch: list[dict]) -> int:
        return 0
