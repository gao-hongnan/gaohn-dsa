from typing import List, Any


class StackList:
    """Creates a stack that uses python's default list as the underlying
    data structure.

    Attributes:
        stack_items (List[Any]): The list that stores the items in the stack.
            We treat the end of the list as the top of the stack.
    """

    _stack_items: List[Any]

    def __init__(self) -> None:
        self._stack_items = []

    @property
    def stack_items(self) -> List[Any]:
        """Read only property for the stack items."""
        return self._stack_items

    def is_empty(self) -> bool:
        """Check if stack is empty.

        Returns:
            (bool): True if stack is empty, False otherwise.
        """
        return self.size == 0

    def push(self, item: Any) -> None:
        """Push an item on top of the stack.

        In this implementation, the item is appended to the end of the list.

        Args:
            item (Any): The current item pushed into the stack.
        """
        self.stack_items.append(item)

    def pop(self) -> Any:
        """Pop an item from the top of the stack.

        In this implementation, the item at the end of the list is returned
        and removed. We are using the list's pop method to do this.

        Raises:
            (Exception): If stack is empty.

        Returns:
            (Any): The top most item in the stack.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack_items.pop()

    def peek(self) -> Any:
        """Return the top most item in the stack without modifying the stack.

        This is different from pop in that it does not remove the item from the
        stack.

        Returns:
            (Any): The top most item in the stack.
        """
        return self.stack_items[-1]

    @property
    def size(self) -> int:
        """Return the size of the stack.

        Returns:
            (int): The size of the stack.
        """
        return len(self.stack_items)
