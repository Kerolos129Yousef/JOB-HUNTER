import httpx

from app.schemas.job import JobSchema
from app.services.html_cleaner import HTMLCleaner
from app.collectors.base import BaseCollector


class GreenhouseCollector(BaseCollector):
    def __init__(self, board: str, company: str):
        self.board = board
        self.company = company

    async def fetch_jobs(self) -> list[JobSchema]:
        url = (
            f"https://boards-api.greenhouse.io/v1/boards/"
            f"{self.board}/jobs?content=true"
        )

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(url)
            response.raise_for_status()

        data = response.json()

        jobs: list[JobSchema] = []

        for job in data["jobs"]:
            jobs.append(
                JobSchema(
                    title=job["title"],
                    company=self.company,
                    location=job.get("location", {}).get("name"),
                    description=HTMLCleaner.clean(job.get("content")),
                    url=job["absolute_url"],
                    source="greenhouse",
                    external_id=str(job.get("id")),
                    raw_data=job,
                )
            )

        return jobs