from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=False, init=True)
class Node(Generic[T]):
    """
    The Node object is initialized with a value and can be linked to the next node by setting the next_node attribute to a Node object.
    This node is Singular associated with Singly Linked List.

    Attributes:
        curr_node_value (Any): The value associated with the created node.
        next_node (Node): The next node in the linked list. Note the distinction between curr_node_value and next_node, the former is the value of the node, the latter is the pointer to the next node.

    Examples:
        >>> node = Node(1)
        >>> print(node.curr_node_value)
        1
        >>> print(node.next_node)
        None
        >>> node.next_node = Node(2)
        >>> print(node.next_node.curr_node_value)
        2
        >>> print(node.next_node.next_node)
        None
    """

    curr_node_value: T
    next_node: Node = None
