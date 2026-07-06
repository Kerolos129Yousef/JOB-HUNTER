from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.db.models import Job
from app.schemas.job_filter import JobFilter

class JobService:
    def __init__(self, db: Session):
        self.db = db

    def get_jobs(self, filters: JobFilter):
        page = filters.page
        size = filters.size
        q = filters.q
        company = filters.company
        location = filters.location
        source = filters.source
        sort = filters.sort
        order = filters.order

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
       
       
        sort_columns = {
            "created_at": Job.created_at,
            "company": Job.company,
            "title": Job.title,
            "score": Job.score,
        }

        column = sort_columns.get(sort, Job.created_at)

        if order == "asc":
            order_by = column.asc()
        else:
            order_by = column.desc()

        items = (
            query
            .order_by(order_by)
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