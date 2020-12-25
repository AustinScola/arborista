"""Transformation for parsing a file from a path."""
from pathlib import Path
from typing import cast

from arborista.node import Node
from arborista.nodes.file_system.file import File
from arborista.nodes.file_system.path_node import PathNode
from arborista.nodes.sequences.text.string import String
from arborista.transformation import Transformation
from arborista.transformation_result import TransformationResult


class PathToFile(Transformation):  # pylint: disable=too-few-public-methods
    """Transformation for parsing a file from a path."""
    NODE_TYPES = {PathNode}

    @classmethod
    def maybe_transform(cls, node: Node) -> TransformationResult:
        node.assert_is_type(cls.NODE_TYPES)

        path_node: PathNode = cast(PathNode, node)
        file_path: Path = path_node.path

        system_file_contents: str
        with open(file_path) as system_file:
            system_file_contents = system_file.read()
        contents: String = String(system_file_contents)

        file_: File = File(file_path, contents)

        transformation_result: TransformationResult = TransformationResult(file_, True, [path_node])

        return transformation_result
