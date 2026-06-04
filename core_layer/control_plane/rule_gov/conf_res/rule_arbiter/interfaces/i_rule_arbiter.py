from typing import Protocol


class IRuleArbiter(Protocol):
    def load_rules(self) -> None:
        pass

    def prioritize(self) -> None:
        pass

    def override(self) -> None:
        pass

    def arbitrate(self) -> None:
        pass
