"""Parses a file."""
from pathlib import Path

from arborista.parser import Parser


class FileParser(Parser):  # pylint: disable=too-few-public-methods
    """Parses a file."""
    @staticmethod
    def parse_file(file_path: Path) -> str:
        """Return the contents of the file as a string."""
        with open(file_path) as file_:
            contents: str = file_.read()
        return contents
