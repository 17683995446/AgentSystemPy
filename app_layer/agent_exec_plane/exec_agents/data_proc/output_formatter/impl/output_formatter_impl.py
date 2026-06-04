from ..interfaces.i_output_formatter import IOutputFormatter
class OutputFormatterImpl(IOutputFormatter):
    def format_data(self) -> None:
        pass

    def apply_style(self) -> None:
        pass

    def wrap_block(self) -> None:
        pass

    def encode_stream(self) -> None:
        pass
