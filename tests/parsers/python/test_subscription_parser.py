"""Test arborista.parsers.python.subscription_parser."""
import libcst
import pytest

from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.name import Name
from arborista.nodes.python.subscription import Subscription
from arborista.nodes.python.subscripts import Subscripts
from arborista.parser import Parser
from arborista.parsers.python.subscription_parser import LibcstSubscription, SubscriptionParser


def test_libcst_subscription() -> None:
    """Test arborista.parsers.python.subscription_parser.LibcstSubscription."""
    assert LibcstSubscription == libcst.Subscript


def test_inheritance() -> None:
    """Test arborista.parsers.python.subscription_parser.SubscriptionParser inheritance."""
    assert issubclass(SubscriptionParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_subscription, expected_subscription', [
    (libcst.Subscript(libcst.Name('foo'), [libcst.SubscriptElement(libcst.Index(libcst.Integer('0')))]), Subscription(Name('foo'), Subscripts(Index(Integer(0)), []))),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_subscription(libcst_subscription: LibcstSubscription,
                            expected_subscription: Subscription) -> None:
    """Test arborista.parsers.python.subscription_parser.SubscriptionParser.parse_subscription."""
    subscription: Subscription = SubscriptionParser.parse_subscription(libcst_subscription)

    assert subscription == expected_subscription
