from app.matcher.bonuses.base import BaseBonus
from app.matcher.models import ScoreResult


class InfrastructureBonus(BaseBonus):

    def apply(self, result: ScoreResult) -> None:

        if result.has_all(
            "docker",
            "kubernetes",
            "terraform",
        ):
            result.add(
                type="bonus",
                value="Infrastructure Stack",
                weight=20,
            )