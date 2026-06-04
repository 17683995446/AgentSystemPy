from ..interfaces.i_log_exporter import ILogExporter
class LogExporterImpl(ILogExporter):
    def export_file(self) -> None:
        pass

    def export_stream(self) -> None:
        pass

    def format_output(self) -> None:
        pass

    def close_export(self) -> None:
        pass
