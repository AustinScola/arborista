"""Test arborista.deparsers.python.greater_than_or_equals_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.greater_than_or_equals_deparser import GreaterThanOrEqualsDeparser
from arborista.nodes.python.greater_than_or_equals import GreaterThanOrEquals


def test_inheritance() -> None:
    """Test arborista.deparsers.python.greater_than_or_equals_deparser.GreaterThanOrEqualsDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(GreaterThanOrEqualsDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('greater_than_or_equals, expected_string', [
    (GreaterThanOrEquals(), '>='),
])
# yapf: enable
def test_deparse_greater_than_or_equals(greater_than_or_equals: GreaterThanOrEquals,
                                        expected_string: str) -> None:
    """Test arborista.deparsers.python.greater_than_or_equals_deparser.GreaterThanOrEqualsDeparser.deparse_greater_than_or_equals."""  # pylint: disable=line-too-long, useless-suppression
    string: str = GreaterThanOrEqualsDeparser.deparse_greater_than_or_equals(greater_than_or_equals)

    assert string == expected_string
