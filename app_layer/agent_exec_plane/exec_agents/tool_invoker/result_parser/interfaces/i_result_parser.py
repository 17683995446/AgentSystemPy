from typing import Protocol


class IResultParser(Protocol):
    def parse_raw(self) -> None:
        pass

    def extract_data(self) -> None:
        pass

    def validate_format(self) -> None:
        pass

    def convert_type(self) -> None:
        pass
