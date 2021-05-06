"""Test arborista.nodes.python.arguments."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.arguments.Arguments inheritance."""
    assert issubclass(Arguments, PythonNode)


_PARENT = MagicMock()


# yapf: disable
@pytest.mark.parametrize('arguments, keyword_arguments, expected_arguments, expected_parent', [
    ([], {}, [], None),
    ([], {'parent': None}, [], None),
    ([], {'parent': _PARENT}, [], _PARENT),
    ([[Name('foo')]], {}, [Name('foo')], None),
    ([[Name('foo'), Name('bar'), Name('baz')]], {}, [Name('foo'), Name('bar'), Name('baz')], None),
])
# yapf: enable
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any],
              expected_arguments: List[Argument], expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.arguments.Arguments.__init__."""
    arguments_node: Arguments = Arguments(*arguments, **keyword_arguments)

    assert arguments_node.arguments == expected_arguments
    assert arguments_node.parent is expected_parent
