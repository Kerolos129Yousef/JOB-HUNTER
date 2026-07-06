from pydantic import BaseModel


class ScoreMatch(BaseModel):
    keyword: str
    weight: int


class ScoreResult(BaseModel):
    score: int
    matches: list[ScoreMatch]