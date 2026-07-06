from sqlalchemy import String, Text, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from app.db.base import Base
from sqlalchemy import JSON
from typing import Any

class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(String(255))

    company: Mapped[str] = mapped_column(String(255))

    location: Mapped[str | None]

    description: Mapped[str | None] = mapped_column(Text())

    url: Mapped[str] = mapped_column(unique=True)

    source: Mapped[str]

    raw_score: Mapped[float] = mapped_column(default=0)

    score: Mapped[int] = mapped_column(default=0)

    score_breakdown: Mapped[dict[str, int] | None] = mapped_column(
        JSON,
        nullable=True,
    )

    score_details: Mapped[list[dict[str, Any]] | None] = mapped_column(
        JSON,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)