from ..interfaces.i_msg_compress_engine import IMsgCompressEngine
class MsgCompressEngineImpl(IMsgCompressEngine):
    def compress(self) -> None:
        pass

    def decompress(self) -> None:
        pass

    def estimate_ratio(self) -> None:
        pass
