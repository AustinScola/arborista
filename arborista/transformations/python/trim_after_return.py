"""Transformation for trimming small statements after a return statement in simple statement."""
from typing import Optional, cast

from arborista.node import Node
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.small_statement import SmallStatementList
from arborista.transformation import Transformation


class TrimAfterReturn(Transformation):  # pylint: disable=too-few-public-methods
    """Transformation for trimming small statements after a return statement in simple statement."""
    @staticmethod
    def maybe_transform(node: Node) -> Optional[Node]:
        """Trim small statements after a return statement in simple statement."""
        node.assert_is_type(SimpleStatement)

        simple_statement: SimpleStatement = cast(SimpleStatement, node)
        small_statements: SmallStatementList = simple_statement.small_statements
        for small_statement_index, small_statement in enumerate(small_statements):
            if isinstance(small_statement, ReturnStatement):
                simple_statement.small_statements = small_statements[:small_statement_index + 1]
                break

        return simple_statement
