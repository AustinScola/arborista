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


# yapf: disable
@pytest.mark.parametrize('first, rest, parent, pass_parent', [
    (Name('foo'), [], None, False),
    (Name('foo'), [], None, True),
    (Name('foo'), [], MagicMock(), True),
    (Name('foo'), [Name('bar'), Name('baz')], None, False),
])
# yapf: enable
def test_init(first: Argument, rest: List[Argument], parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.arguments.Arguments.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    arguments: Arguments = Arguments(first, rest, **keyword_arguments)

    assert arguments.first == first
    assert arguments.rest == rest
    assert arguments.parent is parent
