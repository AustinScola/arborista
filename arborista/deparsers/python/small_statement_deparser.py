"""Deparser for a Python small statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.flow_statement_deparser import FlowStatementDeparser
from arborista.deparsers.python.pass_statement_deparser import PassStatementDeparser
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.pass_statement import PassStatement
from arborista.nodes.python.small_statement import SmallStatement


class SmallStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python small statement."""
    @staticmethod
    def deparse_small_statement(small_statement: SmallStatement) -> str:
        """Deparse a Python small statement."""
        string: str
        if isinstance(small_statement, FlowStatement):
            flow_statement: FlowStatement = small_statement
            string = FlowStatementDeparser.deparse_flow_statement(flow_statement)
            return string
        if isinstance(small_statement, PassStatement):
            pass_statement: PassStatement = small_statement
            string = PassStatementDeparser.deparse_pass_statement(pass_statement)
            return string
        raise NotImplementedError  # pragma: no cover
