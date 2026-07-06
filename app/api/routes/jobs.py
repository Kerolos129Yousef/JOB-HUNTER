from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.services.job_service import JobService
from app.schemas.job_response import (
    JobListResponse,
    JobDetailsResponse,
    JobPageResponse,
)
from fastapi import Query
router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=JobPageResponse)
def get_jobs(
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
    q: str | None = Query(None),
    company: str | None = Query(None),
    location: str | None = Query(None),
    source: str | None = Query(None),
    db: Session = Depends(get_db),
):
    service = JobService(db)

    return service.get_jobs(
        page=page,
        size=size,
        q=q,
        company=company,
        location=location,
        source=source,
    )



@router.get("/{job_id}", response_model=JobDetailsResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    service = JobService(db)

    job = service.get_job(job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    return job