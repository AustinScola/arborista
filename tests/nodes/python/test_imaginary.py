"""Test arborista.nodes.python.imaginary."""
from typing import Any, Dict, Optional, Union

import pytest

from arborista.node import Node
from arborista.nodes.python.imaginary import Imaginary
from arborista.nodes.python.number import Number
from testing_helpers.animal_nodes import Dog


def test_inheritance() -> None:
    """Test arborista.nodes.python.imaginary.Imaginary inheritance."""
    assert issubclass(Imaginary, Number)


# yapf: disable
@pytest.mark.parametrize('value, parent, pass_parent, expected_parent', [
    (0, None, False, None),
    (0.0, None, False, None),
    (0, None, True, None),
    (0.0, None, True, None),
    (0, Dog(), True, Dog()),
    (0.0, Dog(), True, Dog()),

])
# yapf: enable
def test_init(value: Union[int, float], parent: Optional[Node], pass_parent: bool,
              expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.imaginary.Imaginary.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    imaginary = Imaginary(value, **keyword_arguments)

    assert imaginary.value == value
    assert imaginary.parent == expected_parent


# yapf: disable
@pytest.mark.parametrize('imaginary, other, expected_equality', [
    (Imaginary(1), 'foo', False),
    (Imaginary(1), Imaginary(2), False),
    (Imaginary(1), Imaginary(1), True),
])
# yapf: enable
def test_eq(imaginary: Imaginary, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.imaginary.Imaginary.__eq__."""
    equality: bool = imaginary == other

    assert equality == expected_equality
