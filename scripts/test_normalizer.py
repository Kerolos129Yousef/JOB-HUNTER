from app.matcher.normalizer import ScoreNormalizer

for score in [0, 20, 40, 80, 120, 180, 240, 300]:
    print(f"{score:3} -> {ScoreNormalizer.normalize(score)}")