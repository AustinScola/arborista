"""Test arborista.nodes.python.parameter."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.parameter import Parameter
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.simple_statement import SimpleStatement


def test_inheritance() -> None:
    """Test arborista.nodes.python.parameter.Parameter inheritance."""
    assert issubclass(Parameter, PythonNode)


# yapf: disable
@pytest.mark.parametrize('name, parent, pass_parent', [
    (Name('foo'), None, False),
    (Name('foo'), None, True),
    (Name('foo'), FunctionDefinition(Name('foo'), [], SimpleStatement([])), True),
])
# yapf: enable
def test_init(name: Name, parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.parameter.Parameter.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    parameter: Parameter = Parameter(name, **keyword_arguments)

    assert parameter.name == name
    assert id(parameter.parent) == id(parent)


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
