from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class AITitleRule(BaseRule):

    type = "title"

    group = "ai"

    rules = {
        "ai engineer": 25,
        "ml engineer": 25,
        "machine learning": 20,
        "llm": 20,
        "generative ai": 20,
    }

    def apply(
        self,
        text: str,
        result: ScoreResult,
    ):
        self.match_keywords(text, result)