from typing import Protocol


class ILogFileWriter(Protocol):
    def open_file(self, path: str) -> object:
        ...

    def write_record(self, fh: object, record: dict) -> None:
        ...

    def rotate_file(self, fh: object) -> object:
        ...
