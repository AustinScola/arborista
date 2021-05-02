"""Deparser for a Python if statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.suite_deparser import SuiteDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.if_ import If
from arborista.nodes.python.suite import Suite


class IfDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python if statement."""
    @staticmethod
    def deparse_if(if_: If, indent: str) -> str:
        """Deparse a Python if statement."""
        string: str

        from arborista.deparsers.python.expression_deparser import \
            ExpressionDeparser  # pylint: disable=import-outside-toplevel
        condition: Expression = if_.condition
        condition_string: str = ExpressionDeparser.deparse_expression(condition)

        body: Suite = if_.body
        if isinstance(body, Block):
            body_string = '\n' + SuiteDeparser.deparse_suite(body, indent)
        else:
            body_string = SuiteDeparser.deparse_suite(body, '')

        string = f'{indent}if {condition_string}:{body_string}'

        return string
