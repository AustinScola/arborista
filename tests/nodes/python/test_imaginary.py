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
@pytest.mark.parametrize('value, parent, pass_parent', [
    (0, None, False),
    (0.0, None, False),
    (0, None, True),
    (0.0, None, True),
    (0, Dog(), True),
    (0.0, Dog(), True),

])
# yapf: enable
def test_init(value: Union[int, float], parent: Optional[Node], pass_parent: bool) -> None:
    """Test arborista.nodes.python.imaginary.Imaginary.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    imaginary = Imaginary(value, **keyword_arguments)

    assert imaginary.value == value
    assert imaginary.parent is parent
