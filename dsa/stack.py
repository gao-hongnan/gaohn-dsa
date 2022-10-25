from __future__ import annotations

from typing import Generic, TypeVar, List

T = TypeVar("T")


class StackList(Generic[T]):
    """Creates a stack that uses python's default list as the underlying
    data structure.

    Note:
        Methods are ordered with dunder/magic/property -> public -> private -> static/class.

    Attributes:
        stack_items (List[T]): The list that stores the items in the stack.
            We treat the end of the list as the top of the stack.
    """

    _stack_items: List[T]

    def __init__(self) -> None:
        self._stack_items = []

    def __len__(self) -> int:
        """Return the size of the stack."""
        return len(self.stack_items)

    def __iter__(self) -> StackList[T]:
        """Iterate over the stack items.

        Note:
            If we do not define __next__, we can use
            ```
            while not self.is_empty():
                yield self.pop()
            ```

        Returns:
            (StackList[T]): The stack.
        """
        return self

    def __next__(self) -> T:
        """Return the next item in the stack.

        Returns:
            (T): The next item in the stack.
        """
        if self.is_empty():
            raise StopIteration
        return self.pop()

    @property
    def stack_items(self) -> List[T]:
        """Read only property for the stack items."""
        return self._stack_items

    @property
    def size(self) -> int:
        """Return the size of the stack.

        Returns:
            (int): The size of the stack.
        """
        return len(self)

    def is_empty(self) -> bool:
        """Check if stack is empty.

        Returns:
            (bool): True if stack is empty, False otherwise.
        """
        return self.size == 0

    def peek(self) -> T:
        """Return the top most item in the stack without modifying the stack.

        This is different from pop in that it does not remove the item from the
        stack.

        Returns:
            (T): The top most item in the stack.
        """
        return self.stack_items[-1]

    def pop(self) -> T:
        """Pop an item from the top of the stack.

        In this implementation, the item at the end of the list is returned
        and removed. We are using the list's pop method to do this.

        Raises:
            (Exception): If stack is empty.

        Returns:
            (T): The top most item in the stack.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack_items.pop()

    def push(self, item: T) -> None:
        """Push an item on top of the stack.

        In this implementation, the item is appended to the end of the list.

        Args:
            item (T): The current item pushed into the stack.
        """
        self.stack_items.append(item)


if __name__ == "__main__":
    stack = StackList()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(f"stack size = {stack.size}")

    for item in stack:
        print(item)
