"""Test arborista.nodes.python.keyword_argument."""
from typing import Any, Dict, List, Optional
from unittest.mock import MagicMock

import pytest

from arborista.node import Node
from arborista.nodes.python.argument import Argument
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.keyword_argument import KeywordArgument
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.nodes.python.keyword_argument.KeywordArgument inheritance."""
    assert issubclass(KeywordArgument, Argument)


_PARENT = MagicMock()


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('arguments, keyword_arguments, expected_name, expected_value, expected_parent', [
    ([Name('foo'), Name('bar')], {}, Name('foo'), Name('bar'), None),
    ([Name('foo'), Name('bar')], {'parent': None}, Name('foo'), Name('bar'), None),
    ([Name('foo'), Name('bar')], {'parent': _PARENT}, Name('foo'), Name('bar'), _PARENT),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(arguments: List[Any], keyword_arguments: Dict[str, Any], expected_name: Name,
              expected_value: Expression, expected_parent: Optional[Node]) -> None:
    """Test arborista.nodes.python.keyword_argument.KeywordArgument.__init__."""
    keyword_argument: KeywordArgument = KeywordArgument(*arguments, **keyword_arguments)

    assert keyword_argument.name == expected_name
    assert keyword_argument.value == expected_value
    assert keyword_argument.parent is expected_parent
