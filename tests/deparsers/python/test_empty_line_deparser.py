"""Test arborista.deparsers.python.empty_line_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.empty_line_deparser import EmptyLineDeparser
from arborista.nodes.python.empty_line import EmptyLine


def test_inheritance() -> None:
    """Test arborista.deparsers.python.empty_line_deparser.EmptyLineDeparser inheritance."""
    assert issubclass(EmptyLineDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('empty_line, expected_string', [
    (EmptyLine(), '\n'),
])
# yapf: enable
def test_deparse_empty_line(empty_line: EmptyLine, expected_string: str) -> None:
    """Test arborista.deparsers.python.empty_line_deparser.EmptyLineDeparser.deparse_empty_line."""
    string: str = EmptyLineDeparser.deparse_empty_line(empty_line)

    assert string == expected_string
