from app.matcher.models import ScoreResult
from app.matcher.rules.base import BaseRule


class SkillsRule(BaseRule):

    type = "skill"

    rules = {
        "python": 15,
        "docker": 20,
        "kubernetes": 25,
        "terraform": 20,
        "aws": 20,
        "linux": 15,
        "git": 10,
        "ci/cd": 15,
        "grafana": 15,
    }

    # def apply(
    #     self,
    #     text: str,
    #     result: ScoreResult,
    # ):
    #     self.match_keywords(text, result)