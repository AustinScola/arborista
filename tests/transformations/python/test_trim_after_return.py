"""Test arborista.transformations.python.trim_after_return."""
from typing import Optional, Type

import pytest

from arborista.exception import ArboristaException
from arborista.exceptions.unexpected_node_type_exception import UnexpectedNodeTypeException
from arborista.node import Node
from arborista.nodes.python.block import Block
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.transformation import Transformation
from arborista.transformations.python.trim_after_return import TrimAfterReturn


def test_node_types() -> None:
    """Test arborista.python.transformations.trim_after_return.TrimAfterReturn.NODE_TYPES."""
    assert TrimAfterReturn.NODE_TYPES == {SimpleStatement}


def test_inheritance() -> None:
    """Test arborista.python.transformations.trim_after_return.TrimAfterReturn."""
    assert issubclass(TrimAfterReturn, Transformation)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('node, expected_result, expected_exception', [
    (SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()]), None),
    (SimpleStatement([ReturnStatement(), ReturnStatement()]), SimpleStatement([ReturnStatement()]), None),
    (SimpleStatement([ReturnStatement(), ReturnStatement(), ReturnStatement()]), SimpleStatement([ReturnStatement()]), None),
    (Block([SimpleStatement([ReturnStatement()])], indent='    '), None, UnexpectedNodeTypeException),
])
# yapf: enable # pylint: enable=line-too-long
def test_maybe_transform(node: Node, expected_result: Optional[Node],
                         expected_exception: Optional[Type[ArboristaException]]) -> None:
    """Test arborista.python.transformations.trim_after_return.TrimAfterReturn.maybe_transform."""
    if expected_exception:
        with pytest.raises(expected_exception):
            TrimAfterReturn.maybe_transform(node)
    else:
        result: Optional[Node] = TrimAfterReturn.maybe_transform(node)
        assert result == expected_result
