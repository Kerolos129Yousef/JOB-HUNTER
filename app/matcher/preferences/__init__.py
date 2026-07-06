from importlib import import_module
from pathlib import Path


def load_preferences():

    current = Path(__file__).parent

    for file in current.glob("*.py"):

        if file.stem in {"__init__", "base"}:
            continue

        import_module(f"{__name__}.{file.stem}")