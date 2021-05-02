"""Deparser for a Python subscription."""
from arborista.deparser import Deparser
from arborista.deparsers.python.subscripts_deparser import SubscriptsDeparser
from arborista.nodes.python.expression import Expression
from arborista.nodes.python.subscription import Subscription
from arborista.nodes.python.subscripts import Subscripts


class SubscriptionDeparser(Deparser):  # pylint: disable=too-few-public-methods
    """Deparser for a Python subscription."""
    @staticmethod
    def deparse_subscription(subscription: Subscription) -> str:
        """Deparse a Python subscription."""
        string: str

        from arborista.deparsers.python.expression_deparser import \
            ExpressionDeparser  # pylint: disable=import-outside-toplevel

        value: Expression = subscription.value
        value_string: str = ExpressionDeparser.deparse_expression(value)

        subscripts: Subscripts = subscription.subscripts
        subscripts_string: str = SubscriptsDeparser.deparse_subscripts(subscripts)

        string = value_string + '[' + subscripts_string + ']'

        return string
