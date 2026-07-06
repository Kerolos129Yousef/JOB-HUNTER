import httpx

from app.collectors.base import BaseCollector


class AshbyCollector(BaseCollector):
    def __init__(self, board: str, company: str):
        self.board = board
        self.company = company

    async def fetch_jobs(self):
        url = f"https://jobs.ashbyhq.com/api/non-user-graphql?organization={self.board}"

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.get(url)

            print(response.status_code)
            print(response.text[:500])

            return []