"""Test arborista.nodes.python.parameter."""
from typing import Any

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


# yapf: disable
@pytest.mark.parametrize('parameter, other, expected_equality', [
    (Parameter(Name('foo')), 'bar', False),
    (Parameter(Name('foo')), Parameter(Name('foo')), True),
])
# yapf: enable
def test_eq(parameter: Parameter, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.parameter.Parameter.__eq__."""
    equality: bool = parameter == other
    assert equality == expected_equality
