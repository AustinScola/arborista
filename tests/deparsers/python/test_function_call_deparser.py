"""Test arborista.deparsers.python.function_call_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.function_call_deparser import FunctionCallDeparser
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.function_call import FunctionCall
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.function_call_deparser.FunctionCallDeparser inheritance."""
    assert issubclass(FunctionCallDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('function_call, expected_string', [
    (FunctionCall(Name('foo'), Arguments()), 'foo()'),
    (FunctionCall(Name('foo'), Arguments([Name('bar')])), 'foo(bar)'),
    (FunctionCall(Name('foo'), Arguments([Name('bar'), Name('baz')])), 'foo(bar, baz)'),
])
# yapf: enable
def test_deparse_function_call(function_call: FunctionCall, expected_string: str) -> None:
    """Test arborista.deparsers.python.function_call_deparser.FunctionCallDeparser.deparse_function_call."""  # pylint: disable=line-too-long, useless-suppression
    string: str = FunctionCallDeparser.deparse_function_call(function_call)

    assert string == expected_string
