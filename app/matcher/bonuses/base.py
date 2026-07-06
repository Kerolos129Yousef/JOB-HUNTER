from abc import ABC, abstractmethod

from app.matcher.models import ScoreResult


class BaseBonus(ABC):

    registry = []

    def __init_subclass__(cls):
        super().__init_subclass__()

        if cls is not BaseBonus:
            BaseBonus.registry.append(cls())

    @abstractmethod
    def apply(self, result: ScoreResult) -> None:
        """
        Apply bonus if conditions are met.
        """
        pass