"""Test arborista.deparsers.python.newline_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.newline_deparser import NewlineDeparser
from arborista.nodes.python.newline import Newline


def test_inheritance() -> None:
    """Test arborista.deparsers.python.newline_deparser.NewlineDeparser inheritance."""
    assert issubclass(NewlineDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('newline, expected_string', [
    (Newline(), '\n'),
    (Newline('\n'), '\n'),
    (Newline('\r\n'), '\r\n'),
])
# yapf: enable
def test_deparse_newline(newline: Newline, expected_string: str) -> None:
    """Test arborista.deparsers.python.newline_deparser.NewlineDeparser.deparse_newline."""
    string: str = NewlineDeparser.deparse_newline(newline)

    assert string == expected_string
