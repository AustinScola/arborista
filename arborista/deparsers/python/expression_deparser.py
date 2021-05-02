"""A deparser for a Python expression."""
from arborista.deparser import Deparser
from arborista.deparsers.python.atom_deparser import AtomDeparser
from arborista.deparsers.python.comparison_deparser import ComparisonDeparser
from arborista.deparsers.python.function_call_deparser import FunctionCallDeparser
from arborista.deparsers.python.subscription_deparser import SubscriptionDeparser
from arborista.nodes.python.atom import Atom
from arborista.nodes.python.comparison import Comparison
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.function_call import FunctionCall
from arborista.nodes.python.subscription import Subscription


class ExpressionDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """A deparser for a Python expression."""
    @staticmethod
    def deparse_expression(expression: Expression) -> str:
        """Deparse a Python expression."""
        string: str

        if isinstance(expression, Atom):
            atom = expression
            string = AtomDeparser.deparse_atom(atom)
        elif isinstance(expression, Comparison):
            comparison: Comparison = expression
            string = ComparisonDeparser.deparse_comparison(comparison)
        elif isinstance(expression, FunctionCall):
            function_call: FunctionCall = expression
            string = FunctionCallDeparser.deparse_function_call(function_call)
        elif isinstance(expression, Subscription):
            subscription = expression
            string = SubscriptionDeparser.deparse_subscription(subscription)
        else:
            raise NotImplementedError  # pragma: no cover

        return string
