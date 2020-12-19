"""Test arborista.tree."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node
from arborista.tree import Tree
from tests.animal_nodes import Dog


# yapf: disable
@pytest.mark.parametrize('root, pass_root, expected_root', [
    (None, False, None),
    (None, True, None),
    (Dog(), True, Dog()),
])
# yapf: enable
def test_init(root: Optional[Node], pass_root: bool, expected_root: Optional[Node]) -> None:
    """Test arborista.tree.Tree.__init__"""
    keyword_arguments: Dict[str, Any] = {}
    if pass_root:
        keyword_arguments['root'] = root

    tree: Tree = Tree(**keyword_arguments)

    assert tree.root == expected_root
