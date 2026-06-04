from typing import Protocol


class IMsgCompressEngine(Protocol):
    def compress(self) -> None:
        pass

    def decompress(self) -> None:
        pass

    def estimate_ratio(self) -> None:
        pass
