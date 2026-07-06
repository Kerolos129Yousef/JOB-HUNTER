from app.matcher.scoring import JobScorer
from app.schemas.job import JobSchema

job = JobSchema(
    title="Senior DevOps Engineer",
    company="Test",
    location="Remote",
    description="""
    We use Docker, Kubernetes and Terraform.
    Experience with AWS is required.
    """,
    url="test",
    source="test",
)

result = JobScorer().score(job)

print(result.score)

for match in result.matches:
    print(match)