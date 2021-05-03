"""Test arborista.parsers.python.assignment_target_parser."""
from typing import Sequence

import libcst
import pytest

from arborista.nodes.python.assignment_targets import AssignmentTargets
from arborista.nodes.python.name import Name
from arborista.parser import Parser
from arborista.parsers.python.assignment_targets_parser import (AssignmentTargetsParser,
                                                                LibcstAssignmentTargets)


def test_libcst_assignment_targets() -> None:
    """Test arborista.parsers.python.assignment_target_parser.LibcstAssignmentTargets."""
    assert isinstance(LibcstAssignmentTargets, type(Sequence))
    assert LibcstAssignmentTargets.__args__ == (libcst.AssignTarget, )  # type: ignore[attr-defined]


def test_inheritance() -> None:
    """Test arborista.parsers.python.assignment_target_parser.AssignmentTargetsParser inheritance."""  # pylint: disable=line-too-long, useless-suppression
    assert issubclass(AssignmentTargetsParser, Parser)


# yapf: disable # pylint: disable=line-too-long
@pytest.mark.parametrize('libcst_assignment_targets, expected_assignment_targets', [
    ([libcst.AssignTarget(libcst.Name('foo'))], AssignmentTargets(Name('foo'), [])),
    ([libcst.AssignTarget(libcst.Name('foo')), libcst.AssignTarget(libcst.Name('bar'))], AssignmentTargets(Name('foo'), [Name('bar')])),
    ([libcst.AssignTarget(libcst.Name('foo')), libcst.AssignTarget(libcst.Name('bar')), libcst.AssignTarget(libcst.Name('baz'))], AssignmentTargets(Name('foo'), [Name('bar'), Name('baz')])),
])
# yapf: enable # pylint: enable=line-too-long
def test_parse_assignment_targets(libcst_assignment_targets: LibcstAssignmentTargets,
                                  expected_assignment_targets: AssignmentTargets) -> None:
    """Test arborista.parsers.python.assignment_target_parser.AssignmentTargetsParser.parse_assignment_targets."""  # pylint: disable=line-too-long, useless-suppression
    assignment_targets: AssignmentTargets = AssignmentTargetsParser.parse_assignment_targets(
        libcst_assignment_targets)

    assert assignment_targets == expected_assignment_targets
