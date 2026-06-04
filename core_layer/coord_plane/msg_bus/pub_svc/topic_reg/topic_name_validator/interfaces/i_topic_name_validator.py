from typing import Protocol


class ITopicNameValidator(Protocol):
    def validate_name(self) -> None:
        pass

    def sanitize_name(self) -> None:
        pass

    def check_duplicate(self) -> None:
        pass
