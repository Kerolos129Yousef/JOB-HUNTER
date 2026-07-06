from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class ManagementTitleRule(BaseRule):

    type = "title"

    group = "management"

    rules = {
        "engineering manager": 15,
        "technical lead": 20,
        "tech lead": 20,
        "staff engineer": 20,
        "principal engineer": 30,
    }

    def apply(
        self,
        text: str,
        result: ScoreResult,
    ):
        self.match_keywords(text, result)