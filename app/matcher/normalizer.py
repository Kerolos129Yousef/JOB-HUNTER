from math import exp


class ScoreNormalizer:

    MIDPOINT = 120
    STEEPNESS = 0.025

    @classmethod
    def normalize(cls, raw_score: float) -> int:
        """
        Convert raw score to a value between 0 and 100.
        """
        normalized = 100 / (
            1 + exp(-cls.STEEPNESS * (raw_score - cls.MIDPOINT))
        )

        return round(normalized)