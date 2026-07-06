from pydantic import BaseModel, Field
from pydantic import PrivateAttr
from sqlalchemy import values

class ScoreMatch(BaseModel):
    type: str
    value: str
    weight: int
    reason: str | None = None
    group: str | None = None


class ScoreResult(BaseModel):
    score: float = 0

    matches: list[ScoreMatch] = Field(default_factory=list)

    # internal cache
    _groups: dict[str, ScoreMatch] = PrivateAttr(default_factory=dict)

    def add(
        self,
        type: str,
        value: str,
        weight: int,
        group: str | None = None,
    ):

        match = ScoreMatch(
            type=type,
            value=value,
            weight=weight,
            group=group,
        )

        # Rules بدون Group
        if group is None:
            self.matches.append(match)
            self.score += weight
            return

        # أول مرة يظهر فيها الـ Group
        if group not in self._groups:
            self._groups[group] = match
            self.matches.append(match)
            self.score += weight
            return

        # موجود بالفعل
        current = self._groups[group]

        # لو الوزن الجديد أقل أو مساوى نتجاهله
        if weight <= current.weight:
            return

        # لو الوزن أكبر نستبدله
        self.score -= current.weight

        self.matches.remove(current)

        self.matches.append(match)

        self._groups[group] = match

        self.score += weight

    def has(self, value: str) -> bool:
        return any(match.value == value for match in self.matches)


    def has_all(self, *values: str) -> bool:
        return all(self.has(value) for value in values)


    def has_any(self, *values: str) -> bool:
        return any(self.has(value) for value in values)