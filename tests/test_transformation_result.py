"""Test arborista.transformation_result."""
from typing import Any, Optional

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.transformation_result import TransformationResult
from testing_helpers.animal_nodes import Cat, Dog
from testing_helpers.assert_nodes_match import assert_nodes_match


# yapf: disable
@pytest.mark.parametrize('transformed_node, changed, removed_nodes, expected_removed_nodes_list', [
    (None, False, iter(()), []),
    (None, False, iter((Dog(),)), [Dog()]),
    (None, False, iter([Dog()]), [Dog()]),
    (None, False, iter([Dog(), Dog(), Dog()]), [Dog(), Dog(), Dog()]),
    (None, True, iter(()), []),
    (Dog(), False, iter(()), []),
])
# yapf: enable
def test_init(transformed_node: Optional[Node], changed: bool, removed_nodes: NodeIterator,
              expected_removed_nodes_list: NodeList) -> None:
    """Test arborista.transformation_result.TransformationResult.__init__."""
    transformation_result: TransformationResult = TransformationResult(
        transformed_node, changed, removed_nodes)

    assert transformation_result.transformed_node == transformed_node
    assert transformation_result.changed == changed
    assert_nodes_match(transformation_result.removed_nodes, expected_removed_nodes_list)


spot = Dog()
moose = Dog()

aurora = Cat()
petey = Cat()


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('transformation_result, other, expected_equality', [
    (TransformationResult(None, False, []), 'foo', False),
    (TransformationResult(Dog(), False, []), TransformationResult(Cat(), False, []), False),
    (TransformationResult(Dog(), False, []), TransformationResult(Dog(), False, [spot]), False),
    (TransformationResult(Dog(), False, [spot]), TransformationResult(Dog(), False, [moose]), False),
    (TransformationResult(Dog(), False, [spot]), TransformationResult(Dog(), False, [petey]), False),
    (TransformationResult(Dog(), False, [spot, aurora, moose]), TransformationResult(Dog(), False, [spot, petey, moose]), False),
    (TransformationResult(Dog(), False, [spot, aurora, moose]), TransformationResult(Dog(), False, [spot, aurora, petey]), False),
    (TransformationResult(Dog(), True, []), TransformationResult(Dog(), False, []), False),
    (TransformationResult(Dog(), False, []), TransformationResult(Dog(), False, []), True),
    (TransformationResult(Cat(), True, []), TransformationResult(Cat(), True, []), True),
    (TransformationResult(None, True, []), TransformationResult(None, True, []), True),
    (TransformationResult(None, True, [spot]), TransformationResult(None, True, [spot]), True),
    (TransformationResult(None, True, [aurora, spot]), TransformationResult(None, True, [aurora, spot]), True),
    (TransformationResult(None, True, [spot, aurora]), TransformationResult(None, True, [aurora, spot]), True),
    (TransformationResult(None, True, [spot, petey, moose]), TransformationResult(None, True, [petey, spot, moose]), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(transformation_result: TransformationResult, other: Any,
            expected_equality: bool) -> None:
    """Test arborista.transformation_result.TransformationResult.__eq__."""
    equality: bool = transformation_result == other

    assert equality == expected_equality
