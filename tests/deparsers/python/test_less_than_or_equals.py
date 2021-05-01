"""Test arborista.deparsers.python.less_than_or_equals_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.less_than_or_equals_deparser import LessThanOrEqualsDeparser
from arborista.nodes.python.less_than_or_equals import LessThanOrEquals


def test_inheritance() -> None:
    """Test arborista.deparsers.python.less_than_or_equals_deparser.LessThanOrEqualsDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(LessThanOrEqualsDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('less_than_or_equals, expected_string', [
    (LessThanOrEquals(), '<='),
])
# yapf: enable
def test_deparse_less_than_or_equals(less_than_or_equals: LessThanOrEquals,
                                     expected_string: str) -> None:
    """Test arborista.deparsers.python.less_than_or_equals_deparser.LessThanOrEqualsDeparser.deparse_less_than_or_equals."""  # pylint: disable=line-too-long, useless-suppression
    string: str = LessThanOrEqualsDeparser.deparse_less_than_or_equals(less_than_or_equals)

    assert string == expected_string
