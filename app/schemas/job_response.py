from datetime import datetime

from pydantic import BaseModel, ConfigDict


class JobListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    company: str
    location: str | None
    source: str
    score: float
    url: str
    created_at: datetime


class JobDetailsResponse(JobListResponse):
    description: str | None

from math import ceil


class JobPageResponse(BaseModel):
    items: list[JobListResponse]
    total: int
    page: int
    size: int
    pages: int