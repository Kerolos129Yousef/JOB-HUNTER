from sqlalchemy.orm import Session

from app.db.models import Job
from app.schemas import job
from app.schemas.job import JobSchema


class JobRepository:
    def __init__(self, db: Session):
        self.db = db

    def upsert(self, job: JobSchema) -> tuple[Job, bool]:
        """
        Returns:
            (job, created)

            created = True  -> New Job
            created = False -> Existing Job
        """

        existing = (
            self.db.query(Job)
            .filter(Job.url == job.url)
            .first()
        )

        if existing:
            existing.title = job.title
            existing.company = job.company
            existing.location = job.location
            existing.description = job.description
            existing.source = job.source
            existing.score = job.score
            existing.score_details = job.score_details

            self.db.commit()
            self.db.refresh(existing)

            return existing, False

        new_job = Job(
            title=job.title,
            company=job.company,
            location=job.location,
            description=job.description,
            url=job.url,
            source=job.source,
            score=job.score,
            score_details=job.score_details,
        )

        self.db.add(new_job)
        self.db.commit()
        self.db.refresh(new_job)

        return new_job, True