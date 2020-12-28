"""Deparser for a Python flow statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.break_statement_deparser import BreakStatementDeparser
from arborista.deparsers.python.continue_statement_deparser import ContinueStatementDeparser
from arborista.deparsers.python.return_statement_deparser import ReturnStatementDeparser
from arborista.nodes.python.break_statement import BreakStatement
from arborista.nodes.python.continue_statement import ContinueStatement
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.return_statement import ReturnStatement


class FlowStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python flow statement."""
    @staticmethod
    def deparse_flow_statement(flow_statement: FlowStatement) -> str:
        """Deparse a Python flow statement."""
        string: str
        if isinstance(flow_statement, BreakStatement):
            break_statement: BreakStatement = flow_statement
            string = BreakStatementDeparser.deparse_break_statement(break_statement)
            return string
        if isinstance(flow_statement, ContinueStatement):
            continue_statement: ContinueStatement = flow_statement
            string = ContinueStatementDeparser.deparse_continue_statement(continue_statement)
            return string
        if isinstance(flow_statement, ReturnStatement):
            return_statement: ReturnStatement = flow_statement
            string = ReturnStatementDeparser.deparse_return_statement(return_statement)
            return string
        raise NotImplementedError
