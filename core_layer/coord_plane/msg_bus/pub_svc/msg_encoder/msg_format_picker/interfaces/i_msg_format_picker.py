from typing import Protocol


class IMsgFormatPicker(Protocol):
    def detect_format(self) -> None:
        pass

    def pick_encoder(self) -> None:
        pass

    def register_format(self) -> None:
        pass
