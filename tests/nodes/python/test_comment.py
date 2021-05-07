"""Test arborista.nodes.python.comment."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.comment import Comment
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.comment.Comment inheritance."""
    assert issubclass(Comment, PythonNode)


_PARENT = MagicMock()


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_value, expected_parent', [
    (['# foo'], {}, '# foo', None),
    (['# foo'], {'parent': None}, '# foo', None),
    (['# foo'], {'parent': _PARENT}, '# foo', _PARENT),
])
# yapf: enable
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any], expected_value: str,
              expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.comment.Comment.__init__."""
    comment: Comment = Comment(*arguments, **keyword_arguments)

    assert comment.value == expected_value
    assert comment.parent is expected_parent
