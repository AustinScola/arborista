"""Test arborista.deparsers.python.ellipsis_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.ellipsis_deparser import EllipsisDeparser
from arborista.nodes.python.ellipsis_node import EllipsisNode


def test_inheritance() -> None:
    """Test arborista.deparsers.python.ellipsis_deparser.EllipsisDeparser inheritance."""
    assert issubclass(EllipsisDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('ellipsis_node, expected_string', [
    (EllipsisNode(), '...'),
])
# yapf: enable
def test_deparse_ellipsis(ellipsis_node: EllipsisNode, expected_string: str) -> None:
    """Test arborista.deparsers.python.ellipsis_deparser.EllipsisDeparser.deparse_ellipsis."""
    string: str = EllipsisDeparser.deparse_ellipsis(ellipsis_node)

    assert string == expected_string
