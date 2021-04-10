"""Test arborista.deparsers.python.single_quoted_short_string_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.single_quoted_short_string_deparser import \
    SingleQuotedShortStringDeparser
from arborista.nodes.python.single_quoted_short_string import SingleQuotedShortString


def test_inheritance() -> None:
    """Test arborista.deparsers.python.single_quoted_short_string_deparser.SingleQuotedShortStringDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(SingleQuotedShortStringDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('single_quoted_short_string, expected_string', [
    (SingleQuotedShortString(''), "''"),
    (SingleQuotedShortString('foo'), "'foo'"),
])
# yapf: enable
def test_deparser_single_quoted_short_string(single_quoted_short_string: SingleQuotedShortString,
                                             expected_string: str) -> None:
    """Test arborista.deparsers.python.single_quoted_short_string_deparser.SingleQuotedShortStringDeparser.deparse_single_quoted_short_string."""  # pylint: disable=line-too-long, useless-suppression
    string: str = SingleQuotedShortStringDeparser.deparse_single_quoted_short_string(
        single_quoted_short_string)

    assert string == expected_string
