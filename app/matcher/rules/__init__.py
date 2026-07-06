from importlib import import_module
from pathlib import Path


def load_rules():

    rules_dir = Path(__file__).parent

    for file in rules_dir.glob("*.py"):

        if file.stem.startswith("_"):
            continue

        if file.stem in ("base", "__init__"):
            continue

        import_module(f"{__name__}.{file.stem}")