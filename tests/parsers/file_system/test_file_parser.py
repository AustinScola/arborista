"""Test arborista.parsers.file_system.file_parser."""
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from arborista.parser import Parser
from arborista.parsers.file_system.file_parser import FileParser


def test_inheritance() -> None:
    """Test arborista.parsers.file_system.file_parser.FileParser inheritance."""
    assert issubclass(FileParser, Parser)


# yapf: disable
@pytest.mark.parametrize('file_path, file_contents, expected_contents', [
    (Path('foo'), 'bar', 'bar'),
])
# yapf: enable
def test_parse(file_path: Path, file_contents: str, expected_contents: str) -> None:  # pylint: disable=unused-argument
    """Test arborista.parsers.file_system.file_parser.FileParser.parse_file."""
    with patch('builtins.open', mock_open(read_data=file_contents)):
        contents: str = FileParser.parse_file(file_path)

    assert contents == expected_contents
