"""Test arborista.deparsers.python.double_quoted_short_string_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.double_quoted_short_string_deparser import \
    DoubleQuotedShortStringDeparser
from arborista.nodes.python.double_quoted_short_string import DoubleQuotedShortString


def test_inheritance() -> None:
    """Test arborista.deparsers.python.double_quoted_short_string_deparser.DoubleQuotedShortStringDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(DoubleQuotedShortStringDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('double_quoted_short_string, expected_string', [
    (DoubleQuotedShortString("'"), '"\'"'),
    (DoubleQuotedShortString(''), '""'),
    (DoubleQuotedShortString('foo'), '"foo"'),
])
# yapf: enable
def test_deparser_double_quoted_short_string(double_quoted_short_string: DoubleQuotedShortString,
                                             expected_string: str) -> None:
    """Test arborista.deparsers.python.double_quoted_short_string_deparser.DoubleQuotedShortStringDeparser.deparse_double_quoted_short_string."""  # pylint: disable=line-too-long, useless-suppression
    string: str = DoubleQuotedShortStringDeparser.deparse_double_quoted_short_string(
        double_quoted_short_string)

    assert string == expected_string
