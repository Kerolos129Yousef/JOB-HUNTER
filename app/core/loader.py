from pathlib import Path
import json

from app.schemas.board import BoardConfig


DATA_DIR = Path(__file__).resolve().parents[2] / "data"


def load_boards(filename: str) -> list[BoardConfig]:
    path = DATA_DIR / filename

    if not path.exists():
        raise FileNotFoundError(path)

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    return [
        BoardConfig(**item)
        for item in data
        if item.get("enabled", True)
    ]