"""Transformation for deparsing a file."""
from typing import cast

from arborista.node import Node, NodeTypeSet
from arborista.nodes.file_system.file import File
from arborista.nodes.sequences.text.string import String
from arborista.transformation import Transformation
from arborista.transformation_result import TransformationResult


class DeparseFile(Transformation):  # pylint: disable=too-few-public-methods
    """Transformation for deparsing a file."""
    NODE_TYPES: NodeTypeSet = {File}

    @classmethod
    def maybe_transform(cls, node: Node) -> TransformationResult:
        node.assert_is_type(cls.NODE_TYPES)

        transformation_result: TransformationResult
        file_: File = cast(File, node)
        contents: Node = file_.contents

        if not isinstance(contents, String):
            transformation_result = TransformationResult(file_, False, [])
            return transformation_result

        string: String = contents
        string_value: str = string.value
        with open(file_.path, mode='w') as system_file:
            system_file.write(string_value)

        transformation_result = TransformationResult(None, True, [file_])
        return transformation_result
