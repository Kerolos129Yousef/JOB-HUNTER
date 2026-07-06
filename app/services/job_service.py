from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.db.models import Job


class JobService:
    def __init__(self, db: Session):
        self.db = db

    def get_jobs(
        self,
        page: int = 1,
        size: int = 20,
        q: str | None = None,
        company: str | None = None,
        location: str | None = None,
        source: str | None = None,
    ):
        offset = (page - 1) * size

        query = self.db.query(Job)

        if q:
            pattern = f"%{q}%"

            query = query.filter(
                or_(
                    Job.title.ilike(pattern),
                    Job.company.ilike(pattern),
                    Job.description.ilike(pattern),
                )
            )

        if company:
            query = query.filter(Job.company.ilike(f"%{company}%"))

        if location:
            query = query.filter(Job.location.ilike(f"%{location}%"))

        if source:
            query = query.filter(Job.source == source)

        total = query.count()

        items = (
            query
            .order_by(Job.created_at.desc())
            .offset(offset)
            .limit(size)
            .all()
        )

        pages = (total + size - 1) // size

        return {
            "items": items,
            "total": total,
            "page": page,
            "size": size,
            "pages": pages,
        }

    def get_job(self, job_id: int):
        return (
            self.db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )