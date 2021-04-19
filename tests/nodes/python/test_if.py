"""Test arborista.nodes.python.if_."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.if_ import If
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite


def test_inheritance() -> None:
    """Test arborista.nodes.python.if_.If inheritance."""
    assert issubclass(If, PythonNode)


# yapf: disable
@pytest.mark.parametrize('condition, body, parent, pass_parent', [
    (Integer(1), SimpleStatement([PassStatement()]), None, False),
    (Integer(1), SimpleStatement([PassStatement()]), None, True),
    (Integer(1), SimpleStatement([PassStatement()]), MagicMock(), True),
])
# yapf: enable
def test_init(condition: Expression, body: Suite, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.if_.If.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    if_: If = If(condition, body, **keyword_arguments)

    assert if_.condition == condition
    assert if_.body == body
    assert if_.parent is parent
