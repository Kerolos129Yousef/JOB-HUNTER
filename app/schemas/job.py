from pydantic import BaseModel


class JobSchema(BaseModel):
    title: str
    company: str
    location: str | None = None
    description: str | None = None
    url: str
    source: str