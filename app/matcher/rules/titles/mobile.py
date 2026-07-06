from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class MobileTitleRule(BaseRule):

    type = "title"

    group = "mobile"

    rules = {
        "ios engineer": -40,
        "android engineer": -40,
        "mobile engineer": -30,
        "ios developer": -40,
        "android developer": -40,
    }

    def apply(
        self,
        text: str,
        result: ScoreResult,
    ):
        self.match_keywords(text, result)