from ..interfaces.i_result_type_mapper import IResultTypeMapper


class ResultTypeMapperImpl(IResultTypeMapper):
    def map_type(self, raw_value: object, target_type: type) -> object:
        return raw_value

    def coerce_type(self, value: object, target_type: type) -> object:
        return value

    def validate_type(self, value: object, expected_type: type) -> bool:
        return True
