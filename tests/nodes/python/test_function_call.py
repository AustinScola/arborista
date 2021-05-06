"""Test arborista.nodes.python.function_call."""
from typing import Any, Dict, List, Optional
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


_PARENT = MagicMock()


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, keyword_arguments, expected_function, expected_arguments, expected_parent', [
    ([Name('foo')], {}, Name('foo'), Arguments(), None),
    ([Name('foo')], {'parent': None}, Name('foo'), Arguments(), None),
    ([Name('foo')], {'parent': _PARENT}, Name('foo'), Arguments(), _PARENT),
    ([Name('foo'), Arguments()], {'parent': _PARENT}, Name('foo'), Arguments(), _PARENT),
    ([Name('foo'), Arguments([Argument(Name('bar'))])], {}, Name('foo'), Arguments([Argument(Name('bar'))]), None),
    ([Name('foo'), Arguments([Argument(Name('bar')), Argument(Name('baz'))])], {}, Name('foo'), Arguments([Argument(Name('bar')), Argument(Name('baz'))]), None),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(arguments: List[Any], keyword_arguments: Dict[str,
                                                            Any], expected_function: Expression,
              expected_arguments: Arguments, expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.function_call.FunctionCall.__init__"""
    function_call: FunctionCall = FunctionCall(*arguments, **keyword_arguments)

    assert function_call.function == expected_function
    assert function_call.arguments == expected_arguments
    assert function_call.parent is expected_parent
