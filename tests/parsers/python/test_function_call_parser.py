"""Test arborista.parsers.python.function_call_parser."""
import libcst
import pytest

from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.function_call import FunctionCall
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.function_call_parser import FunctionCallParser, LibcstFunctionCall


def test_libcst_funciton_call() -> None:
    """Test arborista.parsers.python.function_call_parser.LibcstFunctionCall."""
    assert LibcstFunctionCall == libcst.Call


def test_inheritance() -> None:
    """Test arborista.parsers.python.function_call_parser.FunctionCallParser inheritance."""
    assert issubclass(FunctionCallParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_function_call, expected_function_call', [
    (libcst.Call(libcst.Name('foo')), FunctionCall(Name('foo'), Arguments())),
    (libcst.Call(libcst.Name('foo'), [libcst.Arg(libcst.Name('bar'))]), FunctionCall(Name('foo'), Arguments([Name('bar')]))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_function_call(libcst_function_call: LibcstFunctionCall,
                             expected_function_call: FunctionCall) -> None:
    """Test arborista.parsers.python.function_call_parser.FunctionCallParser.parse_function_call."""
    function_call: FunctionCall = FunctionCallParser.parse_function_call(libcst_function_call)

    assert function_call == expected_function_call
