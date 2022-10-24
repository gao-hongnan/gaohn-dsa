from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar, Any, List, Optional

T = TypeVar("T")


@dataclass(frozen=False, init=True)
class Node(Generic[T]):
    """
    The `Node` object is initialized with a value and can be linked to the next
    node by setting the `next_node` attribute to a `Node` object.
    This node is singular associated with Singly Linked List.

    Attributes:
        curr_node_value (T): The value associated with the created node.
        next_node (Node): The next node in the linked list.
            Note the distinction between `curr_node_value` and `next_node`,
            the former is the value of the node, the latter is the pointer to
            the next node.

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


class SinglyLinkedList:
    head: Node  # FIXME: self.head = None does not match this type.

    def __init__(self, node_values: Optional[List[T]] = None) -> None:
        self.head = None
        self.node_values = node_values
        if node_values is not None:
            self.add_multiple_nodes()

    def is_empty(self) -> bool:
        """Check if the linked list is empty.

        A linked list is empty if the head is None.

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self.head is None

    def add_multiple_nodes(self) -> None:
        """Add multiple nodes to the linked list.
        Useful when initializing a linked list with multiple values."""

        # do not use self.node_values.pop(0) as it is slow
        first_node = Node(self.node_values[0])
        # set our head to the first node
        self.head = first_node

        for node_value in self.node_values[1:]:
            self.append(node_value)

    def traverse(self) -> str:
        """Traverse through each node in the linked list and return a string.
        Called in __repr__."""
        temp_node = self.head
        string = ""
        while temp_node is not None:
            string += f"{temp_node.curr_node_value} -> "
            temp_node = temp_node.next_node
            if temp_node is None:
                string += "None"
        return string

    def append(self, node_value: T) -> None:
        new_node = Node(node_value)
        if self.is_empty():
            self.head = new_node
            return

        temp_node = self.head
        while temp_node.next_node is not None:
            temp_node = temp_node.next_node

        temp_node.next_node = new_node
        # self.head = temp_node

    def __repr__(self) -> str:
        return self.traverse()

    @property
    def size(self) -> int:
        """Return the size of the linked list.

        Returns:
            (int): The size of the linked list.
        """

        count = 0

        # while self.head is not None:
        #     count += 1
        #     self.head = self.head.next_node

        temp_node = self.head

        while temp_node is not None:
            count += 1
            temp_node = temp_node.next_node

        return count


if __name__ == "__main__":
    first = Node(1)
    second = Node(2)
    third = Node(3)
    ll = SinglyLinkedList()
    ll.head = first
    ll.head.next_node = second
    ll.head.next_node.next_node = third
    print(ll)

    values = [1, 2, 3]
    ll = SinglyLinkedList(values)
    print(ll)

    # # print(ll.head.next_node.next_node.next_node)
    # # print(ll.traverse())
    # print(ll.size)

    # fourth = Node(4)
    # ll.append(fourth)

    # print(ll.head)
    # print(ll.size)
    # # print(ll.head)
