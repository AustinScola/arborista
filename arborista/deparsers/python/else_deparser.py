"""Deparser for a Python else statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.suite_deparser import SuiteDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.else_ import Else
from arborista.nodes.python.suite import Suite


class ElseDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python else statement."""
    @staticmethod
    def deparse_else(else_: Else, indent: str) -> str:
        """Deparse a Python else statement."""
        string: str

        body: Suite = else_.body
        if isinstance(body, Block):
            body_string = '\n' + SuiteDeparser.deparse_suite(body, indent)
        else:
            body_string = SuiteDeparser.deparse_suite(body, '')

        string = f'{indent}else:{body_string}'

        return string
