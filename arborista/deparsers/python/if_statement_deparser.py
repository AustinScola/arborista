"""Deparser for a Python if statement."""
from typing import List, Optional

from arborista.deparser import Deparser
from arborista.deparsers.python.elif_deparser import ElifDeparser
from arborista.deparsers.python.else_deparser import ElseDeparser
from arborista.deparsers.python.if_deparser import IfDeparser
from arborista.nodes.python.elif_ import Elif
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.if_ import If
from arborista.nodes.python.if_statement import IfStatement


class IfStatementDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python if statement."""
    @staticmethod
    def deparse_if_statement(if_statement: IfStatement) -> str:
        """Deparse a Python if statement."""
        string: str

        if_: If = if_statement.if_
        if_string = IfDeparser.deparse_if(if_)

        elifs: List[Elif] = if_statement.elifs
        elif_strings = (ElifDeparser.deparse_elif(elif_) for elif_ in elifs)

        else_: Optional[Else] = if_statement.else_
        if else_ is None:
            string = ''.join((if_string, *elif_strings))
        else:
            else_string = ElseDeparser.deparse_else(else_)
            string = ''.join((if_string, *elif_strings, else_string))

        return string
