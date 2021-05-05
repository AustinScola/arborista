"""Test arborista.deparsers.python.parameters_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.parameters_deparser import ParametersDeparser
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameters import Parameters
from arborista.nodes.python.positional_parameter import PositionalParameter


def test_inheritance() -> None:
    """Test arborista.deparsers.python.parameters_deparser.ParametersDeparser inheritance."""
    assert issubclass(ParametersDeparser, Deparser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('parameters, expected_string', [
    (Parameters(), ''),
    (Parameters([PositionalParameter(Name('foo'))]), 'foo'),
    (Parameters([PositionalParameter(Name('foo')), PositionalParameter(Name('bar')), PositionalParameter(Name('baz'))]), 'foo, bar, baz'),
])
# yapf: enable # pylint: enable=line-too-long
def test_deparse_parameters(parameters: Parameters, expected_string: str) -> None:
    """Test arborista.deparsers.python.parameters_deparser.ParametersDeparser.deparse_parameters."""
    string: str = ParametersDeparser.deparse_parameters(parameters)

    assert string == expected_string
