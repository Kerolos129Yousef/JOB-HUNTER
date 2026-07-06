from pydantic import BaseModel


class BoardConfig(BaseModel):
    board: str
    company: str
    enabled: bool = True
    priority: int = 1