from ..interfaces.i_input_sanitizer import IInputSanitizer
class InputSanitizerImpl(IInputSanitizer):
    def trim_input(self) -> None:
        pass

    def escape_chars(self) -> None:
        pass

    def check_length(self) -> None:
        pass

    def validate_type(self) -> None:
        pass
