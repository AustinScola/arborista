"""Parser for a Python flow statement."""
from arborista.nodes.python.flow_statement import FlowStatement
from arborista.nodes.python.return_statement import ReturnStatement
from arborista.parser import Parser
from arborista.parsers.python.return_statement_parser import (LibcstReturnStatement,
                                                              ReturnStatementParser)

LibcstFlowStatement = LibcstReturnStatement


class FlowStatementParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python flow statement."""
    @staticmethod
    def parse_flow_statement(libcst_flow_statement: LibcstFlowStatement) -> FlowStatement:
        """Parse a Python flow statement."""
        if isinstance(libcst_flow_statement, LibcstReturnStatement):
            libcst_return_statement: LibcstReturnStatement = libcst_flow_statement
            return_statement: ReturnStatement = ReturnStatementParser.parse_return_statement(
                libcst_return_statement)
            flow_statment: FlowStatement = return_statement
            return flow_statment
        raise NotImplementedError
