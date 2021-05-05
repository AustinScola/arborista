"""Test arborista.deparsers.python.positional_parameter_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.positional_parameter_deparser import PositionalParameterDeparser
from arborista.nodes.python.name import Name
from arborista.nodes.python.positional_parameter import PositionalParameter


def test_inheritance() -> None:
    """Test arborista.deparsers.python.positional_parameter_deparser.PositionalParameterDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(PositionalParameterDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('positional_parameter, expected_string', [
    (PositionalParameter(Name('foo')), 'foo'),
])
# yapf: enable
def test_deparse_positional_parameter(positional_parameter: PositionalParameter,
                                      expected_string: str) -> None:
    """Test arborista.deparsers.python.positional_parameter_deparser.PositionalParameterDeparser.deparse_positional_parameter."""  # pylint: disable=line-too-long, useless-suppression
    string: str = PositionalParameterDeparser.deparse_positional_parameter(positional_parameter)

    assert string == expected_string
