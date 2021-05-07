"""Test arborista.nodes.python.trailing_whitespace."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.comment import Comment
from arborista.nodes.python.newline import Newline
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.simple_whitespace import SimpleWhitespace
from arborista.nodes.python.trailing_whitespace import TrailingWhitespace


def test_inheritance() -> None:
    """Test arborista.nodes.python.trailing_whitespace.TrailingWhitespace inheritance."""
    assert issubclass(TrailingWhitespace, PythonNode)


_PARENT = MagicMock()


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, keyword_arguments, expected_whitespace, expected_comment, expected_newline, expected_parent', [
    ([], {}, None, None, Newline(), None),
    ([], {'parent': None}, None, None, Newline(), None),
    ([], {'parent': _PARENT}, None, None, Newline(), _PARENT),
    ([SimpleWhitespace('  ')], {}, SimpleWhitespace('  '), None, Newline(), None),
    ([SimpleWhitespace('  '), Comment('# foo')], {}, SimpleWhitespace('  '), Comment('# foo'), Newline(), None),
    ([SimpleWhitespace('  '), Comment('# foo'), Newline()], {}, SimpleWhitespace('  '), Comment('# foo'), Newline(), None),
])
# yapf: enable # pylint: enable=line-too-long
# pylint: disable=too-many-arguments
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
              expected_whitespace: Optional[SimpleWhitespace], expected_comment: Optional[Comment],
              expected_newline: Newline, expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.trailing_whitespace.TrailingWhitespace.__init__."""
    trailing_whitespace: TrailingWhitespace = TrailingWhitespace(*arguments, **keyword_arguments)

    assert trailing_whitespace.whitespace == expected_whitespace
    assert trailing_whitespace.comment == expected_comment
    assert trailing_whitespace.newline == expected_newline
    assert trailing_whitespace.parent is expected_parent
