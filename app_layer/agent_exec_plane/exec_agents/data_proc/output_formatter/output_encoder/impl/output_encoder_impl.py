from ..interfaces.i_output_encoder import IOutputEncoder


class OutputEncoderImpl(IOutputEncoder):
    def encode_json(self, data: dict) -> str:
        return ""

    def encode_xml(self, data: dict) -> str:
        return ""

    def encode_yaml(self, data: dict) -> str:
        return ""
