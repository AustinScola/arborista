"""Test arborista.nodes.python.decorator."""
from typing import Any, Dict, Iterable, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.arguments import Arguments
from arborista.nodes.python.decorator import Decorator, DecoratorList, Decorators
from arborista.nodes.python.dotted_name import DottedName
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode


def test_inheritance() -> None:
    """Test arborista.nodes.python.decorator.Decorator inheritance."""
    assert issubclass(Decorator, PythonNode)


_PARENT = MagicMock()


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, keyword_arguments, expected_name, expected_arguments, expected_parent', [
    ([Name('foo')], {}, Name('foo'), None, None),
    ([Name('foo')], {'parent': None}, Name('foo'), None, None),
    ([Name('foo')], {'parent': _PARENT}, Name('foo'), None, _PARENT),
    ([Name('foo'), [Arguments([Name('bar')])]], {'parent': _PARENT}, Name('foo'), [Arguments([Name('bar')])], _PARENT),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any], expected_name: DottedName,
              expected_arguments: Optional[Arguments], expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.decorator.Decorator"""
    decorator: Decorator = Decorator(*arguments, **keyword_arguments)

    assert decorator.name == expected_name
    assert decorator.arguments == expected_arguments
    assert decorator.parent is expected_parent


def test_decorators() -> None:
    """Test arborista.nodes.python.decorator.Decorators."""
    assert issubclass(Decorators, Iterable)
    assert Decorators.__args__ == (Decorator, )  # type: ignore[attr-defined]


def test_decorator_list() -> None:
    """Test arborista.nodes.python.decorator.DecoratorList."""
    assert issubclass(DecoratorList, List)
    assert DecoratorList.__args__ == (Decorator, )  # type: ignore[attr-defined]
