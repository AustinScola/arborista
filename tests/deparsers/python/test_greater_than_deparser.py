"""Test arborista.deparsers.python.greater_than_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.greater_than_deparser import GreaterThanDeparser
from arborista.nodes.python.greater_than import GreaterThan


def test_inheritance() -> None:
    """Test arborista.deparsers.python.greater_than_deparser.GreaterThanDeparser inheritance."""
    assert issubclass(GreaterThanDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('greater_than, expected_string', [
    (GreaterThan(), '>'),
])
# yapf: enable
def test_deparse_greater_than(greater_than: GreaterThan, expected_string: str) -> None:
    """Test arborista.deparsers.python.greater_than_deparser.GreaterThanDeparser.deparse_greater_than."""  # pylint: disable=line-too-long, useless-suppression
    string: str = GreaterThanDeparser.deparse_greater_than(greater_than)

    assert string == expected_string
