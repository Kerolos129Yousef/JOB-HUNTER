from pydantic import BaseModel, Field


class JobSchema(BaseModel):
    title: str
    company: str
    location: str | None = None
    description: str | None = None
    url: str
    source: str
    score: int = 0
    score_details: list[dict] = Field(default_factory=list)
    raw_score: float = 0
    score_breakdown: dict[str, int] | None = None