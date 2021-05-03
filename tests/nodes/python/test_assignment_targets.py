"""Test arborista.nodes.python.assignment_targets."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.assignment_targets.AssignmentTargets inheritance."""
    assert issubclass(AssignmentTargets, PythonNode)


# yapf: disable
@pytest.mark.parametrize('first, rest, parent, pass_parent', [
    (Name('foo'), [], None, False),
    (Name('foo'), [], None, True),
    (Name('foo'), [], MagicMock, True),
    (Name('foo'), [Name('bar')], MagicMock, True),
    (Name('foo'), [Name('bar'), Name('baz')], MagicMock, True),
])
# yapf: enable
def test_init(first: Expression, rest: List[Expression], parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.assignment_targets.AssignmentTargets.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    assignment_targets: AssignmentTargets = AssignmentTargets(first, rest, **keyword_arguments)

    assert assignment_targets.first == first
    assert assignment_targets.rest == rest
    assert assignment_targets.parent is parent
