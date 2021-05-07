"""Test arborista.deparsers.python.simple_whitespace_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.simple_whitespace_deparser import SimpleWhitespaceDeparser
from arborista.nodes.python.simple_whitespace import SimpleWhitespace


def test_inheritance() -> None:
    """Test arborista.deparsers.python.simple_whitespace_deparser.SimpleWhitespaceDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(SimpleWhitespaceDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('simple_whitespace, expected_string', [
    (SimpleWhitespace(' '), ' '),
    (SimpleWhitespace('\t'), '\t'),
    (SimpleWhitespace('  '), '  '),
])
# yapf: enable
def test_deparse_simple_whitespace(simple_whitespace: SimpleWhitespace,
                                   expected_string: str) -> None:
    """Test arborista.deparsers.python.simple_whitespace_deparser.SimpleWhitespaceDeparser.deparse_simple_whitespace."""  # pylint: disable=line-too-long, useless-suppression
    string: str = SimpleWhitespaceDeparser.deparse_simple_whitespace(simple_whitespace)

    assert string == expected_string
