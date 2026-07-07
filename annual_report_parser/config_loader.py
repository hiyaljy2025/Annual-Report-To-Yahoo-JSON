import json
from pathlib import Path


class ConfigLoader:
    """
    Loads JSON configuration files from the project's config folder.
    """

    def __init__(self):
        project_root = Path(__file__).resolve().parent.parent
        self.config_folder = project_root / "config"

    def load(self, filename: str) -> dict:
        """
        Load a JSON configuration file.

        Example:
            loader.load("statement_keywords.json")
        """

        config_path = self.config_folder / filename

        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)