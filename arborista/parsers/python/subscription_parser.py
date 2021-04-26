"""A parser for a Python subscription."""

import libcst

from arborista.nodes.python.expression import Expression
from arborista.nodes.python.subscription import Subscription
from arborista.nodes.python.subscripts import Subscripts
from arborista.parser import Parser
from arborista.parsers.python.expression_parser import ExpressionParser, LibcstExpression
from arborista.parsers.python.subscripts_parser import LibcstSubscripts, SubscriptsParser

LibcstSubscription = libcst.Subscript


class SubscriptionParser(Parser):  # pylint: disable=too-few-public-methods
    """A parser for a Python subscription."""
    @staticmethod
    def parse_subscription(libcst_subscription: LibcstSubscription) -> Subscription:
        """Parse a Python subscription."""
        libcst_value: LibcstExpression = libcst_subscription.value
        value: Expression = ExpressionParser.parse_expression(libcst_value)

        libcst_subscripts: LibcstSubscripts = libcst_subscription.slice
        subscripts: Subscripts = SubscriptsParser.parse_subscripts(libcst_subscripts)

        subscription: Subscription = Subscription(value, subscripts)

        return subscription
