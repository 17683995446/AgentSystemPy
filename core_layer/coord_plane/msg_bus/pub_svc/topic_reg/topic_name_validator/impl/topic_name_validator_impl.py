from ..interfaces.i_topic_name_validator import ITopicNameValidator
class TopicNameValidatorImpl(ITopicNameValidator):
    def validate_name(self) -> None:
        pass

    def sanitize_name(self) -> None:
        pass

    def check_duplicate(self) -> None:
        pass
