"""Test arborista.nodes.python.annotated_assignment_statement."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.annotated_assignment_statement import AnnotatedAssignmentStatement
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.name import Name
from arborista.nodes.python.small_statement import SmallStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.annotated_assignment_statement.AnnotatedAssignmentStatement inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(AnnotatedAssignmentStatement, SmallStatement)


# yapf: disable
@pytest.mark.parametrize('target, annotation, value, parent, pass_parent', [
    (Name('foo'), Name('Foo'), None, None, False),
    (Name('foo'), Name('Foo'), Name('bar'), None, False),
    (Name('foo'), Name('Foo'), None, None, True),
    (Name('foo'), Name('Foo'), None, MagicMock(), True),
])
# yapf: enable
def test_init(target: Expression, annotation: Expression, value: Optional[Expression],
              parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.annotated_assignment_statement.AnnotatedAssignmentStatement."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    annotated_assignment_statement: AnnotatedAssignmentStatement = \
        AnnotatedAssignmentStatement(target, annotation, value, **keyword_arguments)

    assert annotated_assignment_statement.target == target
    assert annotated_assignment_statement.annotation == annotation
    assert annotated_assignment_statement.parent is parent
