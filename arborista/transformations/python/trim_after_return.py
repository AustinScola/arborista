"""Transformation for trimming small statements after a return statement in simple statement."""
from typing import Optional, cast

from arborista.exceptions.cannot_find_child_exception import CannotFindChildException
from arborista.node import Node, NodeSequence, NodeTypeSet
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.small_statement import SmallStatementList
from arborista.transformation import Transformation
from arborista.transformation_result import TransformationResult


class TrimAfterReturn(Transformation):  # pylint: disable=too-few-public-methods
    """Transformation for trimming small statements after a return statement in simple statement."""
    NODE_TYPES: NodeTypeSet = {ReturnStatement}

    @classmethod
    def maybe_transform(cls, node: Node) -> TransformationResult:
        """Trim small statements after a return statement in simple statement."""
        node.assert_is_type(cls.NODE_TYPES)
        return_statement: ReturnStatement = cast(ReturnStatement, node)

        changed: bool = False
        removed_nodes: NodeSequence = []

        parent: Optional[Node] = node.parent
        if isinstance(parent, SimpleStatement):
            simple_statement: SimpleStatement = parent
            small_statements: SmallStatementList = simple_statement.small_statements
            return_statement_id = id(return_statement)

            small_statement_index: int
            for small_statement_index, small_statement in enumerate(small_statements):
                if id(small_statement) == return_statement_id:
                    break
            else:
                raise CannotFindChildException()

            if small_statement_index == len(small_statements) - 1:
                return TransformationResult(return_statement, False, [])

            small_statements, removed_nodes = small_statements[:small_statement_index + 1], \
                                              small_statements[small_statement_index + 1:]

            simple_statement.small_statements, changed = small_statements, True
        else:
            raise NotImplementedError
        return TransformationResult(return_statement, changed, removed_nodes)
