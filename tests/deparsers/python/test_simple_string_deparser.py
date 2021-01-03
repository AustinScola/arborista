"""Test arborista.deparsers.python.simple_string_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.simple_string_deparser import SimpleStringDeparser
from arborista.nodes.python.simple_string import SimpleString


def test_inheritance() -> None:
    """Test arborista.deparsers.python.simple_string_deparser.SimpleStringDeparser inheritance."""
    assert issubclass(SimpleStringDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('simple_string, expected_string', [
    (SimpleString("'foo'"), "'foo'"),
])
# yapf: enable
def test_deparse_simple_string(simple_string: SimpleString, expected_string: str) -> None:
    """Test arborista.deparsers.python.simple_string_deparser.SimpleStringDeparser.deparse_simple_string."""  # pylint: disable=line-too-long, useless-suppression
    string: str = SimpleStringDeparser.deparse_simple_string(simple_string)

    assert string == expected_string
