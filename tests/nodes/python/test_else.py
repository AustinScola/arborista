"""Test arborista.nodes.python.else_."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.suite import Suite


def test_inheritance() -> None:
    """Test arborista.nodes.python.else_.Else inheritance."""
    assert issubclass(Else, PythonNode)


# yapf: disable
@pytest.mark.parametrize('body, parent, pass_parent', [
    (SimpleStatement([PassStatement()]), None, False),
    (SimpleStatement([PassStatement()]), None, True),
    (SimpleStatement([PassStatement()]), MagicMock(), True),
])
# yapf: enable
def test_init(body: Suite, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.else_.Else.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    else_: Else = Else(body, **keyword_arguments)

    assert else_.body == body
    assert else_.parent is parent
