from ..interfaces.i_input_normalizer import IInputNormalizer


class InputNormalizerImpl(IInputNormalizer):
    def normalize_whitespace(self, text: str) -> str:
        return text

    def normalize_case(self, text: str, lower: bool = True) -> str:
        return text

    def normalize_encoding(self, text: str, encoding: str = "utf-8") -> str:
        return text
