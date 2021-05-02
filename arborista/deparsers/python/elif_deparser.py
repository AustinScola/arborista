"""Deparser for a Python elif statement."""
from arborista.deparser import Deparser
from arborista.deparsers.python.suite_deparser import SuiteDeparser
from arborista.nodes.python.block import Block
from arborista.nodes.python.elif_ import Elif
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.suite import Suite


class ElifDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python elif statement."""
    @staticmethod
    def deparse_elif(elif_: Elif, indent: str) -> str:
        """Deparse a Python elif statement."""
        string: str

        from arborista.deparsers.python.expression_deparser import \
            ExpressionDeparser  # pylint: disable=import-outside-toplevel
        condition: Expression = elif_.condition
        condition_string: str = ExpressionDeparser.deparse_expression(condition)

        body: Suite = elif_.body
        if isinstance(body, Block):
            body_string = '\n' + SuiteDeparser.deparse_suite(body, indent)
        else:
            body_string = SuiteDeparser.deparse_suite(body, '')

        string = f'{indent}elif {condition_string}:{body_string}'

        return string
