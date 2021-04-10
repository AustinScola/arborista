"""Test arborista.deparsers.python.single_quoted_long_string_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.single_quoted_long_string_deparser import \
    SingleQuotedLongStringDeparser
from arborista.nodes.python.single_quoted_long_string import SingleQuotedLongString


def test_inheritance() -> None:
    """Test arborista.deparsers.python.single_quoted_long_string_deparser.SingleQuotedLongStringDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(SingleQuotedLongStringDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('single_quoted_long_string, expected_string', [
    (SingleQuotedLongString(''), "''''''"),
    (SingleQuotedLongString('foo'), "'''foo'''"),
])
# yapf: enable
def test_deparser_single_quoted_long_string(single_quoted_long_string: SingleQuotedLongString,
                                            expected_string: str) -> None:
    """Test arborista.deparsers.python.single_quoted_long_string_deparser.SingleQuotedLongStringDeparser.deparse_single_quoted_long_string."""  # pylint: disable=line-too-long, useless-suppression
    string: str = SingleQuotedLongStringDeparser.deparse_single_quoted_long_string(
        single_quoted_long_string)

    assert string == expected_string
