from ..interfaces.i_log_file_writer import ILogFileWriter


class LogFileWriterImpl(ILogFileWriter):
    def open_file(self, path: str) -> object:
        return object()

    def write_record(self, fh: object, record: dict) -> None:
        pass

    def rotate_file(self, fh: object) -> object:
        return object()
