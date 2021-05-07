"""Test arborista.nodes.python.simple_whitespace."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.simple_whitespace import SimpleWhitespace


def test_inheritance() -> None:
    """Test arborista.nodes.python.simple_whitespace.SimpleWhitespace inheritance."""
    assert issubclass(SimpleWhitespace, PythonNode)


_PARENT = MagicMock()


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_value, expected_parent', [
    ([' '], {}, ' ', None),
    ([' '], {'parent': None}, ' ', None),
    ([' '], {'parent': _PARENT}, ' ', _PARENT),
    ([' \\ '], {}, ' \\ ', None),
])
# yapf: enable
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any], expected_value: str,
              expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.simple_whitespace.SimpleWhitespace.__init__."""
    simple_whitespace: SimpleWhitespace = SimpleWhitespace(*arguments, **keyword_arguments)

    assert simple_whitespace.value == expected_value
    assert simple_whitespace.parent is expected_parent
