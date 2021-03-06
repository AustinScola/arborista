"""Parser for a Python statement."""
from typing import Sequence, cast

import libcst

from arborista.nodes.python.compound_statement import CompoundStatement
from arborista.nodes.python.empty_line import EmptyLine
from arborista.nodes.python.simple_statement import SimpleStatement
from arborista.nodes.python.statement import Statement, StatementList
from arborista.parser import Parser
from arborista.parsers.python.compound_statement_parser import (CompoundStatementParser,
                                                                LibcstCompoundStatement)
from arborista.parsers.python.empty_line_parser import EmptyLineParser, LibcstEmptyLine
from arborista.parsers.python.simple_statement_parser import (LibcstSimpleStatement,
                                                              SimpleStatementParser)

LibcstStatement = libcst.BaseStatement
LibcstStatements = Sequence[LibcstStatement]


class StatementParser(Parser):
    """Parser for a Python statement."""
    @staticmethod
    def parse_statement(libcst_statement: LibcstStatement) -> Statement:
        """Parser a statement."""
        statement: Statement
        if isinstance(libcst_statement, (libcst.SimpleStatementLine, libcst.SimpleStatementSuite)):
            libcst_simple_statement: LibcstSimpleStatement = libcst_statement
            simple_statement: SimpleStatement = SimpleStatementParser.parse_simple_statement(
                libcst_simple_statement)
            statement = simple_statement
        else:
            libcst_compound_statement: LibcstCompoundStatement = cast(LibcstCompoundStatement,
                                                                      libcst_statement)
            compound_statement: CompoundStatement = CompoundStatementParser.\
                parse_compound_statement(libcst_compound_statement)
            statement = compound_statement
        return statement

    @staticmethod
    def parse_statements(libcst_statements: LibcstStatements) -> StatementList:
        """Parser statements."""
        statements: StatementList = []

        for libcst_statement in libcst_statements:

            if isinstance(
                    libcst_statement,
                (libcst.SimpleStatementLine, libcst.SimpleStatementSuite, LibcstCompoundStatement)):
                if libcst_statement.leading_lines:
                    for leading_line in libcst_statement.leading_lines:
                        libcst_empty_line: LibcstEmptyLine = leading_line
                        empty_line: EmptyLine = EmptyLineParser.parse_empty_line(libcst_empty_line)

                        statements.append(empty_line)

            statement: Statement = StatementParser.parse_statement(libcst_statement)
            statements.append(statement)

        return statements
