"""Test arborista.nodes.nebnf.nebnf_node."""
from abc import ABC

from arborista.node import Node
from arborista.nodes.nebnf.nebnf_node import NEBNFNode


def test_inheritance() -> None:
    """Test arborista.nodes.nebnf.nebnf_node.NEBNFNode inheritance."""
    assert issubclass(NEBNFNode, (Node, ABC))
