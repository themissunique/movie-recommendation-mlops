from pathlib import Path

def validate_file(path: Path):

    if not path.exists():
        raise FileNotFoundError(path)

    if path.stat().st_size == 0:
        raise ValueError(f"{path} is empty.")