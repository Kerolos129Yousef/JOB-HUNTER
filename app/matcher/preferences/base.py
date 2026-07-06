from abc import ABC, abstractmethod

from app.schemas.job import JobSchema
from app.matcher.models import ScoreResult


class BasePreference(ABC):

    registry = []

    def __init_subclass__(cls):
        super().__init_subclass__()

        if cls is not BasePreference:
            BasePreference.registry.append(cls())

    @abstractmethod
    def apply(
        self,
        job: JobSchema,
        result: ScoreResult,
    ) -> None:
        ...