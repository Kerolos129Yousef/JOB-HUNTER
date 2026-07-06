from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class FrontendTitleRule(BaseRule):

    type = "title"

    group = "frontend"

    rules = {
        "frontend engineer": 30,
        "frontend developer": 30,
        "front-end engineer": 30,
        "front-end developer": 30,
        "react developer": 25,
        "ui engineer": 20,
    }

    def apply(
        self,
        text: str,
        result: ScoreResult,
    ):
        self.match_keywords(text, result)