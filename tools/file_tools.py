from pathlib import Path


def read_file(filename: str) -> str:
    path = Path(filename)

    if not path.exists():
        return "File does not exist."

    return path.read_text()


def write_file(filename: str, content: str) -> str:
    path = Path(filename)

    path.write_text(content)

    return f"File {filename} written successfully."