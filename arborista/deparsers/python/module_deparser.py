"""Deparser for a Python module."""
from typing import Iterator

from arborista.deparser import Deparser
from arborista.deparsers.python.statement_deparser import StatementDeparser
from arborista.nodes.python.module import Module


class ModuleDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python module."""
    @staticmethod
    def deparse_module(module: Module) -> str:
        """Deparse a Python module."""
        statement_strings: Iterator[str] = (StatementDeparser.deparse_statement(statement,
                                                                                indent='')
                                            for statement in module.statements)
        string: str = ''.join(statement_strings)
        return string
