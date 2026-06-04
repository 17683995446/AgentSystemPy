from typing import Protocol


class ILogExporter(Protocol):
    def export_file(self) -> None:
        pass

    def export_stream(self) -> None:
        pass

    def format_output(self) -> None:
        pass

    def close_export(self) -> None:
        pass
