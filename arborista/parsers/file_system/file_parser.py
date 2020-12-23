"""Parses a file."""
from pathlib import Path

from arborista.nodes.file_system.file import File
from arborista.parser import Parser
from arborista.nodes.sequences.text.string import String


class FileParser(Parser):  # pylint: disable=too-few-public-methods
    """Parses a file."""
    @staticmethod
    def parse_file(file_path: Path) -> File:
        """Parse a file."""
        with open(file_path) as system_file:
            contents: str = system_file.read()

        string: String = String(contents)

        file_: File = File(file_path, string)

        return file_
