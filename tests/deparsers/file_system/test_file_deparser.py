"""Test arborista.deparsers.file_system.file_deparser."""
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

from arborista.deparser import Deparser
from arborista.deparsers.file_system.file_deparser import FileDeparser
from arborista.nodes.file_system.file import File


def test_inheritance() -> None:
    """Test arborista.deparsers.file_system.file_deparser.FileDeparser inheritance."""
    assert issubclass(FileDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('file_', [
    (File(Path('foo'), 'bar')),
])
# yapf: enable
def test_deparse_file(file_: File) -> None:
    """Test arborista.deparsers.file_system.file_deparser.FileDeparser.deparse_file."""
    with patch('builtins.open', mock_open()) as open_mock:
        FileDeparser.deparse_file(file_)

        mock_file = open_mock()
        assert mock_file.write.called_once_with(file_.contents)
