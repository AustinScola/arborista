"""Test arborista.deparsers.python.string_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.string_deparser import StringDeparser
from arborista.nodes.python.double_quoted_long_string import DoubleQuotedLongString
from arborista.nodes.python.double_quoted_short_string import DoubleQuotedShortString
from arborista.nodes.python.single_quoted_long_string import SingleQuotedLongString
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString
from arborista.nodes.python.string import String
from arborista.nodes.python.string_prefix import StringPrefix


def test_inheritance() -> None:
    """Test arborista.deparsers.python.string_deparser.StringDeparser inheritance."""
    assert issubclass(StringDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('string_node, expected_string', [
    (String(None, SingleQuotedShortString('foo')), "'foo'"),
    (String(None, DoubleQuotedShortString('foo')), '"foo"'),
    (String(None, SingleQuotedLongString('foo')), "'''foo'''"),
    (String(None, DoubleQuotedLongString('foo')), '"""foo"""'),
    (String(StringPrefix('f'), SingleQuotedShortString('foo')), "'foo'"),
    (String(StringPrefix('f'), DoubleQuotedShortString('foo')), '"foo"'),
    (String(StringPrefix('f'), SingleQuotedLongString('foo')), "'''foo'''"),
    (String(StringPrefix('f'), DoubleQuotedLongString('foo')), '"""foo"""'),
])
# yapf: enable
def test_deparse_string(string_node: String, expected_string: str) -> None:
    """Test arborista.deparsers.python.string_deparser.StringDeparser.deparse_string."""
    string = StringDeparser.deparse_string(string_node)

    assert string == expected_string
