from statistics import mean, median

from app.db.session import SessionLocal
from app.db.models import Job


db = SessionLocal()

scores = [
    job.score
    for job in db.query(Job).all()
]

db.close()

scores.sort()

print(f"Jobs      : {len(scores)}")
print(f"Min Score : {min(scores)}")
print(f"Max Score : {max(scores)}")
print(f"Mean      : {mean(scores):.2f}")
print(f"Median    : {median(scores):.2f}")


def percentile(data, p):
    index = int((len(data) - 1) * p / 100)
    return data[index]


print()

for p in [50, 60, 70, 75, 80, 85, 90, 95, 99]:
    print(f"P{p:<2} = {percentile(scores, p)}")