"""Test arborista.deparsers.python.assignment_targets_deparser."""
import pytest

from arborista.deparser import Deparser
from arborista.deparsers.python.assignment_targets_deparser import AssignmentTargetsDeparser
from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.name import Name


def test_inheritance() -> None:
    """Test arborista.deparsers.python.assignment_targets_deparser.AssignmentTargetsDeparser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(AssignmentTargetsDeparser, Deparser)


# yapf: disable
@pytest.mark.parametrize('assignment_targets, expected_string', [
    (AssignmentTargets(Name('foo'), []), 'foo'),
    (AssignmentTargets(Name('foo'), [Name('bar')]), 'foo, bar'),
    (AssignmentTargets(Name('foo'), [Name('bar'), Name('baz')]), 'foo, bar, baz'),
])
# yapf: enable
def test_deparse_assignment_targets(assignment_targets: AssignmentTargets,
                                    expected_string: str) -> None:
    """Test arborista.deparsers.python.assignment_targets_deparser.AssignmentTargetsDeparser.deparse_assignment_targets."""  # pylint: disable=line-too-long, useless-suppression
    string: str = AssignmentTargetsDeparser.deparse_assignment_targets(assignment_targets)

    assert string == expected_string
