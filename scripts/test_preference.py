from app.matcher.scoring import JobScorer
from app.schemas.job import JobSchema

job = JobSchema(
    title="Software Engineer",
    company="Datadog",
    location="Remote",
    description="Python Docker Kubernetes",
    url="test",
    source="test",
)

result = JobScorer().score(job)

print(result.score)

for match in result.matches:
    print(match)