"""Test arborista.parsers.python.positional_parameter_parser."""
import libcst
import pytest

from arborista.nodes.python.name import Name
from arborista.nodes.python.positional_parameter import PositionalParameter
from arborista.parser import Parser
from arborista.parsers.python.positional_parameter_parser import (LibcstPositionalParameter,
                                                                  PositionalParameterParser)
from testing_helpers.assert_parent_set_in_children import assert_parent_set_in_children


def test_inheritance() -> None:
    """Test arborista.parsers.python.positional_parameter_parser.PositionalParameterParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(PositionalParameterParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_positional_parameter, expected_positional_parameter', [
    (libcst.Param(libcst.Name('foo'), libcst.Annotation(libcst.Name('Foo'))), PositionalParameter(Name('foo'), Name('Foo'))),
    (libcst.Param(libcst.Name('foo'), libcst.Annotation(libcst.Name('Foo')), default=libcst.Name('bar')), PositionalParameter(Name('foo'), Name('Foo'), Name('bar'))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_positional_parameter(libcst_positional_parameter: LibcstPositionalParameter,
                                    expected_positional_parameter: PositionalParameter) -> None:
    """Test arborista.parsers.python.positional_parameter_parser.PositionalParameterParser.parse_positional_parameter."""  # pylint: disable=line-too-long, useless-suppression
    positional_parameter: PositionalParameter = \
        PositionalParameterParser.parse_positional_parameter(libcst_positional_parameter)

    assert positional_parameter == expected_positional_parameter
    assert_parent_set_in_children(positional_parameter)
