from app.matcher.preferences import load_preferences
from app.matcher.preferences.base import BasePreference
from app.schemas.job import JobSchema

from app.matcher.models import ScoreResult
from app.matcher.rules import load_rules
from app.matcher.rules.base import BaseRule
from app.matcher.bonuses.base import BaseBonus
from app.matcher.bonuses import load_bonuses
from app.matcher.bonuses.base import BaseBonus

class JobScorer:

    def __init__(self):
        load_rules()
        load_bonuses()
        load_preferences()

        

        self.rules = BaseRule.registry

    def score(self, job: JobSchema):

        text = f"""
        {job.title}
        {job.location or ""}
        {job.description or ""}
        """.lower()

        result = ScoreResult()

        for rule in self.rules:
            rule.apply(text, result)


        for bonus in BaseBonus.registry:
            bonus.apply(result)

        for preference in BasePreference.registry:
            preference.apply(job, result)


        result.score = max(result.score, 0)


        return result
    