import html

from bs4 import BeautifulSoup


class HTMLCleaner:
    @staticmethod
    def clean(content: str | None) -> str:
        """
        Convert HTML to clean plain text.

        Example:
            <h1>Hello</h1><p>World</p>
            =>
            Hello World
        """

        if not content:
            return ""

        # Decode HTML entities
        content = html.unescape(content)

        # Remove HTML tags
        soup = BeautifulSoup(content, "html.parser")

        # Return plain text
        return soup.get_text(separator=" ", strip=True)