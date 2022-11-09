from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar, List, Optional

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
    """
    The SinglyLinkedList object is initialized with a head node.

    The `head` node (the first node) of a **Linked List** is of a `Node` object.
    The `head` **entirely determines** the entirety of the whole **Linked List**.
    Because knowing the head node of the **Linked List**, we will be able to
    know every single node that comes after it sequentially (if exists).

    Attributes:
        head (Node): The head node of the linked list.
    """

    head: Node
    node_values: List[T]

    def __init__(self, node_values: Optional[List[T]] = None) -> None:
        self.head = None  # should really be Node(None) in case mypy complains
        self.node_values = node_values

        if node_values is not None:
            self.add_multiple_nodes()

    def __repr__(self) -> str:
        return self.traverse()

    def __iter__(self) -> None:
        temp = self.head
        while temp is not None:
            yield temp, temp.curr_node_value  # yield the node and the node value
            temp = temp.next_node

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

    def insert(self, node_value: T) -> None:
        """Insert a node at the beginning of the linked list.

        Time Complexity:
            O(1) since we are inserting at the beginning.

        Args:
            node_value (T): The value of the node to be inserted at the beginning of the linked list.
        """
        new_node = Node(node_value)
        if self.is_empty():
            self.head = new_node
            return

        new_node.next_node = self.head
        self.head = new_node

    def append(self, node_value: T) -> None:
        """Append a node to the end of the linked list.

        Note:
            If our ll.head is 1 -> 2 -> 3 -> None, and we want to append 4,
            at each loop
            loop 1: we can say temp_node = ll.head.next_node now points to Node(2)
            loop 2: we can say temp_node = ll.head.next_node.next_node now points to Node(3)
            there is no loop 3 because temp_node.next_node.next_node is None after loop 2
            i.e. we can say temp_node = ll.head.next_node.next_node.next_node now points to None

            Recall currently temp_node is Node(3) and temp_node.next_node is None
            so we set temp_node.next_node to be the new_node
            so now Node(3).next_node is Node(4)
            this is equivalent to saying ll.head.next_node.next_node.next_node = Node(4)
            so now the linked list is 1 -> 2 -> 3 -> 4 -> None

        Time Complexity:
            O(n) since need traverse. If we had a tail pointer, we could do O(1)?

        Args:
            node_value (T): The value of the node to be appended to the linked list.
        """

        new_node = Node(node_value)
        if self.is_empty():
            self.head = new_node
            return

        # the head defines the whole linked list 1->2->3->None
        temp_node = self.head  # temp_node is now pointing to the first node Node(1)
        # traverse to the last node
        while temp_node.next_node is not None:
            temp_node = temp_node.next_node

        temp_node.next_node = new_node

    def remove(self, node_value_to_remove: T) -> None:
        """Remove a node from the linked list. Note it removes the first occurrence of the node."""
        if self.is_empty():
            raise ValueError("Cannot remove from an empty linked list.")

        if self.head.curr_node_value == node_value_to_remove:  # first case
            # set the head to the next node, essentially removing the first node
            self.head = self.head.next_node
            return

        previous_node = self.head
        for node, node_value in self:
            if node_value == node_value_to_remove:
                previous_node.next_node = (
                    node.next_node
                )  # link the previous node to the next node
                return

            previous_node = node  # if the if clause is not true, we continue searching by updating the previous_node to be the current node

        raise ValueError(f"{node_value_to_remove} not found in linked list.")

    def search(self):
        pass

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
    for node, node_value in ll:
        print(node, node_value)

    # values = [1, 2, 3]
    # ll = SinglyLinkedList(values)
    # print(ll)

    # # print(ll.head.next_node.next_node.next_node)
    # # print(ll.traverse())
    # print(ll.size)

    fourth = 4
    ll.append(fourth)
    # ll.append_v2(fourth)
    print(ll)
    print(ll.head)

    ll.remove(4)
    print(ll.head)
