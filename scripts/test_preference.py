from app.matcher.scoring import JobScorer
from app.schemas.job import JobSchema

job = JobSchema(
    title="Senior DevOps Engineer",
    company="Datadog",
    location="Remote",
    description="""
    Python
    Docker
    Kubernetes
    """,
    url="test",
    source="test",
)

result = JobScorer().score(job)

print("Final Score:", result.score)
print("Breakdown:", result.breakdown)

print("\nMatches:")
for match in result.matches:
    print(f"{match.type:10} {match.value:25} {match.weight:+}")

for match in result.matches:
    print(match)