from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class PenaltiesRule(BaseRule):

    type = "penalty"

    rules = {
        "ios": -50,
        "android": -50,
        "swift": -40,
        "objective-c": -40,
        "react native": -30,
    }

    # def apply(
    #     self,
    #     text: str,
    #     result: ScoreResult,
    # ):
    #     self.match_keywords(text, result)