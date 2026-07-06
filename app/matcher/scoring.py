from app.schemas.job import JobSchema

from app.matcher.rules.skills import SKILLS
from app.matcher.rules.titles import TITLES
from app.matcher.rules.locations import LOCATIONS
from app.matcher.rules.seniority import SENIORITY
from app.matcher.rules.penalties import PENALTIES
from app.matcher.models import ScoreMatch, ScoreResult


class JobScorer:

    def score(self, job: JobSchema) -> ScoreResult:

        text = f"""
        {job.title}
        {job.location or ""}
        {job.description or ""}
        """.lower()

        matches = []

        matches.extend(self._apply_rules(text, SKILLS))
        matches.extend(self._apply_rules(text, TITLES))
        matches.extend(self._apply_rules(text, LOCATIONS))
        matches.extend(self._apply_rules(text, SENIORITY))
        matches.extend(self._apply_rules(text, PENALTIES))

        score = sum(match.weight for match in matches)

        return ScoreResult(
            score=max(score, 0),
            matches=matches,
        )

    @staticmethod
    def _apply_rules(
        text: str,
        rules: dict[str, int],
    ) -> list[ScoreMatch]:

        matches = []

        for keyword, weight in rules.items():
            if keyword in text:
                matches.append(
                    ScoreMatch(
                        keyword=keyword,
                        weight=weight,
                    )
                )

        return matches