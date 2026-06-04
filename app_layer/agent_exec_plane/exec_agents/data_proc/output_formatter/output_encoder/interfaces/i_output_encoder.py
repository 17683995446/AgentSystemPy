from typing import Protocol


class IOutputEncoder(Protocol):
    def encode_json(self, data: dict) -> str:
        ...

    def encode_xml(self, data: dict) -> str:
        ...

    def encode_yaml(self, data: dict) -> str:
        ...
