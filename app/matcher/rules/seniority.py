from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class SeniorityRule(BaseRule):

    type = "seniority"

    group = "seniority"

    rules = {
        "intern": -20,
        "junior": -10,
        "mid": 5,
        "senior": 10,
        "staff": 20,
        "principal": 30,
    }

    # def apply(
    #     self,
    #     text: str,
    #     result: ScoreResult,
    # ):
    #     self.match_keywords(text, result)