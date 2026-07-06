from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class SecurityTitleRule(BaseRule):

    type = "title"

    group = "security"

    rules = {
        "security engineer": 40,
        "application security": 40,
        "cloud security": 35,
        "security analyst": 25,
        "security architect": 35,
    }

    def apply(
        self,
        text: str,
        result: ScoreResult,
    ):
        self.match_keywords(text, result)