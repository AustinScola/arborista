"""Test arborista.python.nodes.block."""
from typing import Any, Dict, Optional

import pytest

from arborista.node import Node, NodeIterator, NodeList
from arborista.nodes.python.block import Block
from arborista.nodes.python.function_definition import FunctionDefinition
from arborista.nodes.python.name import Name
from arborista.nodes.python.python_node import PythonNode
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.statement import StatementList, Statements


def test_inheritance() -> None:
    """Test arborista.nodes.python.block.Block inheritance."""
    assert issubclass(Block, PythonNode)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('body, expected_body, indent, parent, pass_parent', [
    ([ReturnStatement()], [ReturnStatement()], '    ', None, False),
    ([ReturnStatement()], [ReturnStatement()], '    ', None, True),
    ([ReturnStatement()], [ReturnStatement()], '    ', FunctionDefinition(Name('foo'), [], Block([], '    ')), True),
    ([ReturnStatement()], [ReturnStatement()], '\t', None, False),
    ([ReturnStatement()], [ReturnStatement()], '\t', None, True),
    ([ReturnStatement()], [ReturnStatement()], '\t', FunctionDefinition(Name('foo'), [], Block([], '    ')), True),
    ([ReturnStatement(), ReturnStatement(), ReturnStatement()], [ReturnStatement(), ReturnStatement(), ReturnStatement()], '    ', None, False),
    ([ReturnStatement(), ReturnStatement(), ReturnStatement()], [ReturnStatement(), ReturnStatement(), ReturnStatement()], '    ', None, True),
    ([ReturnStatement(), ReturnStatement(), ReturnStatement()], [ReturnStatement(), ReturnStatement(), ReturnStatement()], '    ', FunctionDefinition(Name('foo'), [], Block([], '    ')), True),
    ([ReturnStatement(), ReturnStatement(), ReturnStatement()], [ReturnStatement(), ReturnStatement(), ReturnStatement()], '\t', None, False),
    ([ReturnStatement(), ReturnStatement(), ReturnStatement()], [ReturnStatement(), ReturnStatement(), ReturnStatement()], '\t', None, True),
    ([ReturnStatement(), ReturnStatement(), ReturnStatement()], [ReturnStatement(), ReturnStatement(), ReturnStatement()], '\t', FunctionDefinition(Name('foo'), [], Block([], '    ')), True),
    (iter([]), [], '   ', None, False),
    (iter([]), [], '   ', None, True),
    (iter([]), [], '   ', FunctionDefinition(Name('foo'), [], Block([], '    ')), True),
    (iter([]), [], '\t', None, False),
    (iter([]), [], '\t', None, True),
    (iter([]), [], '\t', FunctionDefinition(Name('foo'), [], Block([], '    ')), True),
    (iter([ReturnStatement(), ReturnStatement(), ReturnStatement()]), [ReturnStatement(), ReturnStatement(), ReturnStatement()], '    ', None, False),
    (iter([ReturnStatement(), ReturnStatement(), ReturnStatement()]), [ReturnStatement(), ReturnStatement(), ReturnStatement()], '    ', None, True),
    (iter([ReturnStatement(), ReturnStatement(), ReturnStatement()]), [ReturnStatement(), ReturnStatement(), ReturnStatement()], '    ', FunctionDefinition(Name('foo'), [], Block([], '    ')), True),
    (iter([ReturnStatement(), ReturnStatement(), ReturnStatement()]), [ReturnStatement(), ReturnStatement(), ReturnStatement()], '\t', None, False),
    (iter([ReturnStatement(), ReturnStatement(), ReturnStatement()]), [ReturnStatement(), ReturnStatement(), ReturnStatement()], '\t', None, True),
    (iter([ReturnStatement(), ReturnStatement(), ReturnStatement()]), [ReturnStatement(), ReturnStatement(), ReturnStatement()], '\t', FunctionDefinition(Name('foo'), [], Block([], '    ')), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_init(body: Statements, expected_body: StatementList, indent: str, parent: Optional[Node],
              pass_parent: bool) -> None:
    """Test arborista.nodes.python.block.Block.__init__."""
    keyword_arguments: Dict[str, Any] = {}
    if pass_parent:
        keyword_arguments['parent'] = parent

    block: Block = Block(body, indent, **keyword_arguments)

    assert block.body == expected_body
    assert block.indent == indent
    assert block.parent is parent


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('block, other, expected_equality', [
    (Block([SimpleStatement([ReturnStatement()])], '   '), 'foo', False),
    (Block([SimpleStatement([ReturnStatement()])], '   '), Block([SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()])], '   '), False),
    (Block([SimpleStatement([ReturnStatement()])], '   '), Block([SimpleStatement([ReturnStatement()])], '   '), True),
])
# yapf: enable # pylint: enable=line-too-long
def test_eq(block: Block, other: Any, expected_equality: bool) -> None:
    """Test arborista.nodes.python.block.Block.__eq__."""
    equality: bool = block == other

    assert equality == expected_equality


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('block, expected_children_list', [
    (Block([SimpleStatement([ReturnStatement()])], '   '), [SimpleStatement([ReturnStatement()])]),
    (Block([SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()])], '   '), [SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()])]),
    (Block([SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()])], '   '), [SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()]), SimpleStatement([ReturnStatement()])]),
])
# yapf: enable # pylint: enable=line-too-long
def test_iterate_children(block: Block, expected_children_list: NodeList) -> None:
    """Test arborista.nodes.python.block.Block.iterate_children."""
    children: NodeIterator = block.iterate_children()
    children_list: NodeList = list(children)

    assert children_list == expected_children_list
