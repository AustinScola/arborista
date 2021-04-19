"""Test arborista.nodes.python.elif_."""
from typing import Any, Dict, Iterable, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.elif_ import Elif, Elifs
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite


def test_inheritance() -> None:
    """Test arborista.nodes.python.elif_.Elif inheritance."""
    assert issubclass(Elif, PythonNode)


# yapf: disable
@pytest.mark.parametrize('condition, body, parent, pass_parent', [
    (Integer(1), SimpleStatement([PassStatement()]), None, False),
    (Integer(1), SimpleStatement([PassStatement()]), None, True),
    (Integer(1), SimpleStatement([PassStatement()]), MagicMock(), True),
])
# yapf: enable
def test_init(condition: Expression, body: Suite, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.elif_.Elif.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    elif_: Elif = Elif(condition, body, **keyword_arguments)

    assert elif_.condition == condition
    assert elif_.body == body
    assert elif_.parent is parent


def test_elifs() -> None:
    """Test arborista.nodes.python.elif_.Elifs."""
    assert isinstance(Elifs, type(Iterable))
    assert Elifs.__args__ == (Elif, )  # type: ignore[attr-defined]
