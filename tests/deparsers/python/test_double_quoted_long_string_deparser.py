"""Test arborista.deparsers.python.double_quoted_long_string_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.double_quoted_long_string_deparser import \
    DoubleQuotedLongStringDeparser
from arborista.nodes.python.double_quoted_long_string import DoubleQuotedLongString


def test_inheritance() -> None:
    """Test arborista.deparsers.python.double_quoted_long_string_deparser.DoubleQuotedLongStringDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(DoubleQuotedLongStringDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('double_quoted_long_string, expected_string', [
    (DoubleQuotedLongString(''), '""""""'),
    (DoubleQuotedLongString('foo'), '"""foo"""'),
])
# yapf: enable
def test_deparser_double_quoted_long_string(double_quoted_long_string: DoubleQuotedLongString,
                                            expected_string: str) -> None:
    """Test arborista.deparsers.python.double_quoted_long_string_deparser.DoubleQuotedLongStringDeparser.deparse_double_quoted_long_string."""  # pylint: disable=line-too-long, useless-suppression
    string: str = DoubleQuotedLongStringDeparser.deparse_double_quoted_long_string(
        double_quoted_long_string)

    assert string == expected_string
