from pydantic import BaseModel


class JobFilter(BaseModel):
    page: int = 1
    size: int = 20

    q: str | None = None
    company: str | None = None
    location: str | None = None
    source: str | None = None

    sort: str = "created_at"
    order: str = "desc"