"""Test arborista.parsers.python.parameter_parser."""
import libcst
import pytest

from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter, ParameterList
from arborista.parser import Parser
from arborista.parsers.python.parameter_parser import (LibcstParameter, LibcstParameters,
                                                       ParameterParser)
from testing_helpers.assert_parent_set_in_children import assert_parent_set_in_children


def test_inheritance() -> None:
    """Test arborista.parsers.python.parameter_parser.ParameterParser inheritance."""
    assert issubclass(ParameterParser, Parser)


# yapf: disable
@pytest.mark.parametrize('libcst_parameter, expected_parameter', [
    (libcst.Param(libcst.Name('foo')), Parameter(Name('foo'))),
])
# yapf: enable
def test_parse_parameter(libcst_parameter: LibcstParameter, expected_parameter: Parameter) -> None:
    """Test arborista.parsers.python.parameter_parser.ParameterParser.parse_parameter."""
    parameter: Parameter = ParameterParser.parse_parameter(libcst_parameter)

    assert parameter == expected_parameter
    assert_parent_set_in_children(parameter)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_parameters, expected_parameters', [
    (libcst.Parameters(), []),
    (libcst.Parameters([libcst.Param(libcst.Name('foo'))]), [Parameter(Name('foo'))]),
    (libcst.Parameters([libcst.Param(libcst.Name('foo')), libcst.Param(libcst.Name('bar')), libcst.Param(libcst.Name('baz'))]), [Parameter(Name('foo')), Parameter(Name('bar')), Parameter(Name('baz'))]),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_parameters(libcst_parameters: LibcstParameters,
                          expected_parameters: ParameterList) -> None:
    """Test arborista.parsers.python.parameter_parser.ParameterParser.parse_parameters."""
    parameters: ParameterList = ParameterParser.parse_parameters(libcst_parameters)

    assert parameters == expected_parameters
    for parameter in parameters:
        assert_parent_set_in_children(parameter)
