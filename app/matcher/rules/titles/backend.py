from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class BackendTitleRule(BaseRule):

    type = "title"

    group = "backend"

    rules = {
        "backend engineer": 35,
        "backend developer": 35,
        "software engineer": 25,
        "software developer": 25,
        "python developer": 30,
        "python engineer": 30,
    }

    def apply(
        self,
        text: str,
        result: ScoreResult,
    ):
        self.match_keywords(text, result)