import json
from pathlib import Path
from typing import Any


def load_json_file(file_path: str | Path) -> Any:
	"""Read and return the contents of a UTF-8 JSON file."""
	with Path(file_path).open("r", encoding="utf-8") as file:
		return json.load(file)
