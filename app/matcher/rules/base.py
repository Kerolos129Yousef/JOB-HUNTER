from abc import ABC

from app.matcher.models import ScoreResult


class BaseRule(ABC):

    registry = []

    type: str = ""
    group: str | None = None
    rules: dict[str, int] = {}

    def __init_subclass__(cls):
        super().__init_subclass__()

        if cls is not BaseRule:
            BaseRule.registry.append(cls())

    def apply(
        self,
        text: str,
        result: ScoreResult,
    ) -> None:
        self.match_keywords(text, result)

    def match_keywords(
        self,
        text: str,
        result: ScoreResult,
    ) -> None:

        for keyword, weight in self.rules.items():

            if keyword in text:

                result.add(
                    type=self.type,
                    value=keyword,
                    weight=weight,
                    group=self.group,
                )