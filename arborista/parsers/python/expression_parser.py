"""Parser for a Python expression."""
import libcst

from arborista.nodes.python.atom import Atom
from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_call import FunctionCall
from arborista.nodes.python.subscription import Subscription
from arborista.parser import Parser
from arborista.parsers.python.atom_parser import AtomParser, LibcstAtom
from arborista.parsers.python.comparison_parser import ComparisonParser, LibcstComparison
from arborista.parsers.python.function_call_parser import FunctionCallParser, LibcstFunctionCall
from arborista.parsers.python.name_parser import LibcstName
from arborista.parsers.python.number_parser import LibcstNumber
from arborista.parsers.python.subscription_parser import LibcstSubscription, SubscriptionParser

LibcstExpression = libcst.BaseExpression


class ExpressionParser(Parser):  # pylint: disable=too-few-public-methods
    """Parser for a Python expression statement."""
    @staticmethod
    def parse_expression(libcst_expression: LibcstExpression) -> Expression:
        """Parse a Python expression statement."""
        expression: Expression

        from arborista.parsers.python.dotted_name_parser import \
            LibcstDottedName  # pylint: disable=import-outside-toplevel

        if isinstance(libcst_expression, (LibcstName, LibcstDottedName, LibcstNumber,
                                          libcst.SimpleString, libcst.FormattedString)):
            libcst_atom: LibcstAtom = libcst_expression
            atom: Atom = AtomParser.parse_atom(libcst_atom)
            expression = atom
        elif isinstance(libcst_expression, libcst.Comparison):
            libcst_comparison: LibcstComparison = libcst_expression
            comparison: Comparison = ComparisonParser.parse_comparison(libcst_comparison)
            expression = comparison
        elif isinstance(libcst_expression, LibcstFunctionCall):
            libcst_function_call: LibcstFunctionCall = libcst_expression
            function_call: FunctionCall = FunctionCallParser.parse_function_call(
                libcst_function_call)
            expression = function_call
        elif isinstance(libcst_expression, LibcstSubscription):
            libcst_subscription: LibcstSubscription = libcst_expression
            subscription: Subscription = SubscriptionParser.parse_subscription(libcst_subscription)
            expression = subscription
        else:
            raise NotImplementedError(f'Parsing of {type(libcst_expression)} is not implemented yet.')  # pragma: no cover  # pylint: disable=line-too-long, useless-suppression
        return expression
