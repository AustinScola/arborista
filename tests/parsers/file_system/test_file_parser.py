"""Test arborista.parsers.file_system.file_parser."""
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from arborista.nodes.file_system.file import File
from arborista.nodes.sequences.text.string import String
from arborista.parser import Parser
from arborista.parsers.file_system.file_parser import FileParser


def test_inheritance() -> None:
    """Test arborista.parsers.file_system.file_parser.FileParser inheritance."""
    assert issubclass(FileParser, Parser)


# yapf: disable
@pytest.mark.parametrize('file_path, file_contents, expected_file', [
    (Path('foo'), 'bar', File(Path('foo'), String('bar'))),
])
# yapf: enable
def test_parse_file(file_path: Path, file_contents: str, expected_file: File) -> None:
    """Test arborista.parsers.file_system.file_parser.FileParser.parse_file."""
    with patch('builtins.open', mock_open(read_data=file_contents)):
        file_: File = FileParser.parse_file(file_path)

    assert file_ == expected_file
