"""Test arborista.nodes.python.class_definition."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.class_definition import ClassDefinition
from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.name import Name
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite


def test_inheritance() -> None:
    """Test arborista.nodes.python.class_definition.ClassDefinition inheritance."""
    assert issubclass(ClassDefinition, CompoundStatement)


# yapf: disable
@pytest.mark.parametrize('name, bases, body, parent, pass_parent', [
    (Name('Foo'), [], SimpleStatement([PassStatement()]), None, False),
    (Name('Foo'), [], SimpleStatement([PassStatement()]), None, True),
    (Name('Foo'), [], SimpleStatement([PassStatement()]), MagicMock, True),
    (Name('Foo'), [Name('Bar')], SimpleStatement([PassStatement()]), MagicMock, True),
])
# yapf: enable
def test_init(name: Name, bases: Optional[Arguments], body: Suite, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.class_definition.ClassDefinition.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    class_definition: ClassDefinition = ClassDefinition(name, bases, body, **keyword_arguments)

    assert class_definition.name == name
    assert class_definition.body == body
    assert class_definition.bases == bases
    assert class_definition.parent is parent
