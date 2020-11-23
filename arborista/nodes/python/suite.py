"""A Python suite."""
from typing import Union

from arborista.nodes.python.block import Block
from arborista.nodes.python.simple_statement import SimpleStatement

Suite = Union[SimpleStatement, Block]
