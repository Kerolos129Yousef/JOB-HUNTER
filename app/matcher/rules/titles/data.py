from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class DataTitleRule(BaseRule):

    type = "title"

    group = "data"

    rules = {
        "data engineer": 30,
        "data platform": 25,
        "analytics engineer": 25,
        "data scientist": 15,
        "machine learning engineer": 20,
    }

    def apply(
        self,
        text: str,
        result: ScoreResult,
    ):
        self.match_keywords(text, result)