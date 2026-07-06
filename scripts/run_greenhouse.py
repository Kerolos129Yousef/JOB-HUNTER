import asyncio

from app.collectors.collectorsManager import CollectorManager
from app.db.session import SessionLocal
from app.services.job_repository import JobRepository


async def main():
    db = SessionLocal()
    repo = JobRepository(db)

    manager = CollectorManager()

    created = 0
    updated = 0

    try:
        for collector in manager.get_collectors():

            print(f"\nCollecting {collector.company}...")

            try:
                jobs = await collector.fetch_jobs()
            except Exception as e:
                print(f"❌ Failed to collect {collector.company}: {e}")
                continue

            print(f"Found {len(jobs)} jobs")

            for job in jobs:
                _, is_created = repo.upsert(job)

                if is_created:
                    created += 1
                else:
                    updated += 1

        print("\n==============================")
        print(f"Created : {created}")
        print(f"Updated : {updated}")

    finally:
        db.close()


if __name__ == "__main__":
    asyncio.run(main())