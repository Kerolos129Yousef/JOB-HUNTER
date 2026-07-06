from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class InfrastructureTitleRule(BaseRule):

    type = "title"

    group = "infrastructure"

    rules = {
        "devops": 40,
        "site reliability engineer": 40,
        "sre": 40,
        "platform engineer": 35,
        "systems engineer": 30,
        "infrastructure engineer": 30,
        "cloud engineer": 35,
        "DevSecOps Engineer": 35,
    }

    def apply(
        self,
        text: str,
        result: ScoreResult,
    ):
        self.match_keywords(text, result)