import httpx

from app.collectors.base import BaseCollector
from app.schemas.job import JobSchema
from app.services.html_cleaner import HTMLCleaner


class LeverCollector(BaseCollector):
    def __init__(self, board: str, company: str):
        self.board = board
        self.company = company

    async def fetch_jobs(self) -> list[JobSchema]:
        url = f"https://api.lever.co/v0/postings/{self.board}?mode=json"

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(url)
            response.raise_for_status()

        data = response.json()

        jobs = []

        for job in data:
            jobs.append(
                JobSchema(
                    title=job["text"],
                    company=self.company,
                    location=job.get("categories", {}).get("location"),
                    description=HTMLCleaner.clean(job.get("description")),
                    url=job["hostedUrl"],
                    source="lever",
                    external_id=job.get("id"),
                    raw_data=job,
                )
            )

        return jobs