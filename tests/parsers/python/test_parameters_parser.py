"""Test arborista.parsers.python.parameters_parser."""
import libcst
import pytest

from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.positional_parameter import PositionalParameter
from arborista.parser import Parser
from arborista.parsers.python.parameters_parser import LibcstParameters, ParametersParser


def test_libcst_parameters() -> None:
    """Test arborista.parsers.python.parameters_parser.LibcstParameters."""
    assert LibcstParameters == libcst.Parameters


def test_inheritance() -> None:
    """Test arborista.parsers.python.parameters_parser.ParametersParser inheritance."""
    assert issubclass(ParametersParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_parameters, expected_parameters', [
    (libcst.Parameters([]), Parameters()),
    (libcst.Parameters([libcst.Param(libcst.Name('foo'))]), Parameters([PositionalParameter(Name('foo'))])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_parameters(libcst_parameters: LibcstParameters,
                          expected_parameters: Parameters) -> None:
    """Test arborista.parsers.python.parameters_parser.ParametersParser.parse_parameters."""
    parameters: Parameters = ParametersParser.parse_parameters(libcst_parameters)

    assert parameters == expected_parameters
