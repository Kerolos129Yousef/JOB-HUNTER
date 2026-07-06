from datetime import datetime
from typing import Any

from alembic.environment import Any
from pydantic import BaseModel, ConfigDict


class JobListResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    company: str
    location: str | None
    source: str
    score: float
    score_details: list[dict[str, Any]] | None = None
    url: str
    created_at: datetime
    
    model_config = {
        "from_attributes": True
    }

class JobDetailsResponse(JobListResponse):
    description: str | None

from math import ceil


class JobPageResponse(BaseModel):
    items: list[JobListResponse]
    total: int
    page: int
    size: int
    pages: int