from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class LocationsRule(BaseRule):

    type = "location"

    group = "location"

    rules = {
        "remote": 20,
        "hybrid": 5,
    }

    # def apply(
    #     self,
    #     text: str,
    #     result: ScoreResult,
    # ):
    #     self.match_keywords(text, result)