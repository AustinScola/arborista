"""Deparser for a Python small statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.flow_statement_deparser import FlowStatementDeparser
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.small_statement import SmallStatement


class SmallStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python small statement."""
    @staticmethod
    def deparse_small_statement(small_statement: SmallStatement) -> str:
        """Deparse a Python small statement."""
        if isinstance(small_statement, FlowStatement):
            flow_statement: FlowStatement = small_statement
            string: str = FlowStatementDeparser.deparse_flow_statement(flow_statement)
            return string
        raise NotImplementedError
