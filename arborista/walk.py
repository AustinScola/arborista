"""A walk is an iterator of all nodes in a tree."""
from itertools import chain
from typing import Optional

from arborista.node import Node, NodeIterator, NodeList
from arborista.tree import Tree


class Walk():
    """An iterator of all nodes in a tree."""
    def __init__(self, tree: Tree):
        self.tree: Tree = tree
        self.steps: NodeIterator

    def __iter__(self) -> NodeIterator:
        root: Optional[Node] = self.tree.root

        initial_steps: NodeList
        if root is None:
            initial_steps = []
        else:
            initial_steps = [root]

        self.steps = iter(initial_steps)
        return self

    def __next__(self) -> Node:
        step: Node = next(self.steps)
        self.steps = chain(self.steps, step.iterate_children())
        return step
