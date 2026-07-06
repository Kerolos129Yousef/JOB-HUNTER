from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class JobListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    company: str
    location: str | None
    source: str

    raw_score: float
    score: int

    score_breakdown: dict[str, int] | None = None

    score_details: list[dict[str, Any]] | None = None

    url: str
    created_at: datetime


class JobDetailsResponse(JobListResponse):
    description: str | None


class JobPageResponse(BaseModel):
    items: list[JobListResponse]

    total: int
    page: int
    size: int
    pages: int