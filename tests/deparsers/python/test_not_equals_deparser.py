"""Test arborista.deparsers.python.not_equals_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.not_equals_deparser import NotEqualsDeparser
from arborista.nodes.python.not_equals import NotEquals


def test_inheritance() -> None:
    """Test arborista.deparsers.python.not_equals_deparser.NotEqualsDeparser inheritance."""
    assert issubclass(NotEqualsDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('not_equals, expected_string', [
    (NotEquals(), '!='),
])
# yapf: enable
def test_deparse_not_equals(not_equals: NotEquals, expected_string: str) -> None:
    """Test arborista.deparsers.python.not_equals_deparser.NotEqualsDeparser.deparse_not_equals."""
    string: str = NotEqualsDeparser.deparse_not_equals(not_equals)

    assert string == expected_string
