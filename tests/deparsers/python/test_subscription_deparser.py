"""Test arborista.deparsers.python.subscription_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.subscription_deparser import SubscriptionDeparser
from arborista.nodes.python.index import Index
from arborista.nodes.python.integer import Integer
from arborista.nodes.python.name import Name
from arborista.nodes.python.subscription import Subscription
from arborista.nodes.python.subscripts import Subscripts


def test_inheritance() -> None:
    """Test arborista.deparsers.python.subscription_deparser.SubscriptionDeparser inheritance."""
    assert issubclass(SubscriptionDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('subscription, expected_string', [
    (Subscription(Name('foo'), Subscripts(Index(Integer(0)), [])), 'foo[0]'),
])
# yapf: enable
def test_deparse_subscription(subscription: Subscription, expected_string: str) -> None:
    """Test arborista.deparsers.python.subscription_deparser.SubscriptionDeparser.deparse_subscription."""  # pylint: disable=line-too-long, useless-suppression
    string: str = SubscriptionDeparser.deparse_subscription(subscription)

    assert string == expected_string
