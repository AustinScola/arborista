"""Test arborista.nodes.python.parameter."""
import pytest

from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.parameter.Parameter inheritance."""
    assert issubclass(Parameter, PythonNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('name', [
    (Name('foo')),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(name: Name) -> None:
    """Test arborista.nodes.python.parameter.Parameter.__init__."""
    parameter: Parameter = Parameter(name)

    assert parameter.name == name
