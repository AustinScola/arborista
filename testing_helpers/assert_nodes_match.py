"""Assertion helper for asserting that a set of nodes matches an expected set of nodes."""
import pytest

from arborista.node import List, NodeIterable, NodeList


def assert_nodes_match(nodes: NodeIterable, expected_nodes: NodeList) -> None:
    """Assert that a set of nodes matches an expected set of nodes."""
    __tracebackhide__ = True  # pylint: disable=unused-variable
    unexpected_nodes: NodeList = []
    expected_nodes_not_found = expected_nodes

    for node in nodes:
        try:
            expected_nodes_not_found.remove(node)
        except ValueError:
            unexpected_nodes.append(node)

    if unexpected_nodes or expected_nodes_not_found:

        failure_messages: List[str] = []
        if unexpected_nodes:
            unexpected_nodes_string: str = ' '.join(map(str, unexpected_nodes))
            failure_messages.append(f'Unexpected node(s): {unexpected_nodes_string}')
        if expected_nodes_not_found:
            expected_nodes_string: str = ' '.join(map(str, expected_nodes))
            failure_messages.append(f'Expected node(s): {expected_nodes_string}')

        message: str = '\n'.join(failure_messages)
        pytest.fail(message)
