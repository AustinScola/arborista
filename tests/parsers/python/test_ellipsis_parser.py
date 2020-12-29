"""Test arborista.parsers.python.ellipsis_parser."""
import libcst
import pytest

from arborista.nodes.python.ellipsis_node import EllipsisNode
from arborista.parser import Parser
from arborista.parsers.python.ellipsis_parser import EllipsisParser, LibcstEllipsis


def test_inheritance() -> None:
    """Test arborista.parsers.python.ellipsis_parser.EllipsisParser inheritance."""
    assert issubclass(EllipsisParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_ellipsis, expected_ellipsis_node', [
    (libcst.Ellipsis(), EllipsisNode()),
])
# yapf: enable
def test_parse_ellipsis(libcst_ellipsis: LibcstEllipsis,
                        expected_ellipsis_node: EllipsisNode) -> None:
    """Test arborista.parsers.python.ellipsis_parser.EllipsisParser.parse_ellipsis."""
    ellipsis_node: EllipsisNode = EllipsisParser.parse_ellipsis(libcst_ellipsis)

    assert ellipsis_node == expected_ellipsis_node
