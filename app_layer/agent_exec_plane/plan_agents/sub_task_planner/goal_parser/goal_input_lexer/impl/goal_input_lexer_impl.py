from ..interfaces.i_goal_input_lexer import IGoalInputLexer


class GoalInputLexerImpl(IGoalInputLexer):
    def lex_input(self, raw_input: str) -> list[str]:
        return []

    def tokenize(self, lexed: list[str]) -> list[dict]:
        return []

    def classify_token(self, token: dict) -> str:
        return ""
