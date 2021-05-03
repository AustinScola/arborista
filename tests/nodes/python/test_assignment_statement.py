"""Test arborista.nodes.python.assignment_statement."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.assignment_statement import AssignmentStatement
from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.name import Name
from arborista.nodes.python.small_statement import SmallStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.assignment_statement.AssignmentStatement inheritance."""
    assert issubclass(AssignmentStatement, SmallStatement)


# yapf: disable
@pytest.mark.parametrize('targets, value, parent, pass_parent', [
    (AssignmentTargets(Name('foo'), []), Name('bar'), None, False),
    (AssignmentTargets(Name('foo'), []), Name('bar'), None, True),
    (AssignmentTargets(Name('foo'), []), Name('bar'), MagicMock(), True),
])
# yapf: enable
def test_init(targets: AssignmentTargets, value: Expression, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.assignment_statement.AssignmentStatement.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    assignment_statement: AssignmentStatement = AssignmentStatement(targets, value,
                                                                    **keyword_arguments)

    assert assignment_statement.targets == targets
    assert assignment_statement.value == value
    assert assignment_statement.parent is parent
