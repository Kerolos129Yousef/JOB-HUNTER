import re

from app.matcher.aliases import ALIASES


class TextNormalizer:

    _patterns = [
        (
            re.compile(rf"\b{re.escape(alias)}\b"),
            canonical,
        )
        for canonical, aliases in ALIASES.items()
        for alias in aliases
    ]

    @classmethod
    def normalize(cls, text: str) -> str:
        text = text.lower()

        for pattern, canonical in cls._patterns:
            text = pattern.sub(canonical, text)

        return text