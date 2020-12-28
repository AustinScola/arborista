"""Test arborista.deparsers.python.parameter_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.parameter_deparser import ParameterDeparser
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter


def test_inheritance() -> None:
    """Test arborista.deparsers.python.parameter_deparser.ParameterDeparser inheritance."""
    assert issubclass(ParameterDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('parameter, expected_string', [
    (Parameter(Name('foo')), 'foo'),
])
# yapf: enable
def test_deparse_parameter(parameter: Parameter, expected_string: str) -> None:
    """Test arborista.deparsers.python.parameter_deparser.ParameterDeparser.deparse_parameter."""
    string: str = ParameterDeparser.deparse_parameter(parameter)

    assert string == expected_string
