from ..interfaces.i_pub_svc import IPubSvc


class PubSvcImpl(IPubSvc):
    def publish_msg(self, topic: str, msg: dict) -> bool:
        msg["topic"] = topic
        return True

    def broadcast_msg(self, msg: dict) -> bool:
        msg["broadcast"] = True
        return True

    def validate_msg(self, msg: dict) -> bool:
        valid = "body" in msg
        return valid

    def route_msg(self, msg: dict, target: str) -> bool:
        msg["target"] = target
        return True
