"""Test arborista.deparsers.python.less_greater_than_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.less_greater_than_deparser import LessGreaterThanDeparser
from arborista.nodes.python.less_greater_than import LessGreaterThan


def test_inheritance() -> None:
    """Test arborista.deparsers.python.less_greater_than_deparser.LessGreaterThanDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(LessGreaterThanDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('less_greater_than, expected_string', [
    (LessGreaterThan(), '<>'),
])
# yapf: enable
def test_deparse_less_greater_than(less_greater_than: LessGreaterThan,
                                   expected_string: str) -> None:
    """Test arborista.deparsers.python.less_greater_than_deparser.LessGreaterThanDeparser.deparse_less_greater_than."""  # pylint: disable=line-too-long, useless-suppression
    string: str = LessGreaterThanDeparser.deparse_less_greater_than(less_greater_than)

    assert string == expected_string
