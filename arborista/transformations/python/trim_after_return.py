"""Transformation for trimming small statements after a return statement in simple statement."""
from typing import Optional, cast

from arborista.node import Node, NodeTypeSet
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.small_statement import SmallStatementList
from arborista.transformation import Transformation


class TrimAfterReturn(Transformation):  # pylint: disable=too-few-public-methods
    """Transformation for trimming small statements after a return statement in simple statement."""
    NODE_TYPES: NodeTypeSet = {SimpleStatement}

    @classmethod
    def maybe_transform(cls, node: Node) -> Optional[Node]:
        """Trim small statements after a return statement in simple statement."""
        node.assert_is_type(cls.NODE_TYPES)

        simple_statement: SimpleStatement = cast(SimpleStatement, node)
        small_statements: SmallStatementList = simple_statement.small_statements
        for small_statement_index, small_statement in enumerate(small_statements):
            if isinstance(small_statement, ReturnStatement):
                simple_statement.small_statements = small_statements[:small_statement_index + 1]
                break

        return simple_statement
