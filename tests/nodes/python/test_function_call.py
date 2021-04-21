"""Test arborista.nodes.python.function_call."""
from typing import Any, Dict, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_call import FunctionCall
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.nodes.python.function_call.FunctionCall inheritance."""
    assert issubclass(FunctionCall, Expression)


# yapf: disable
@pytest.mark.parametrize('function, arguments, parent, pass_parent', [
    (Name('foo'), None, None, False),
    (Name('foo'), None, None, True),
    (Name('foo'), None, MagicMock(), True),
    (Name('foo'), None, MagicMock(), True),
    (Name('foo'), Arguments(Argument(Name('bar')), [Argument(Name('baz'))]), None, False),
])
# yapf: enable
def test_init(function: Expression, arguments: Optional[Arguments], parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.function_call.FunctionCall.__init__"""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    function_call: FunctionCall = FunctionCall(function, arguments, **keyword_arguments)

    assert function_call.function == function
    assert function_call.arguments == arguments
    assert function_call.parent is parent
