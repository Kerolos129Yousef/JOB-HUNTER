from abc import ABC, abstractmethod

from app.schemas.job import JobSchema


class BaseCollector(ABC):
    @abstractmethod
    async def fetch_jobs(self) -> list[JobSchema]:
        """Fetch and normalize jobs."""
        raise NotImplementedError