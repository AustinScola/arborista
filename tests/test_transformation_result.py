"""Test arborista.transformation_result."""
from typing import Optional

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.transformation_result import TransformationResult
from testing_helpers.animal_nodes import Dog
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
