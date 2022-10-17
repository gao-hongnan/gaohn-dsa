from typing import List, Any


class StackList:
    """Creates a stack that uses python's default list as the underlying
    data structure.

    Attributes:
        stack_items (List[Any]): The list that stores the items in the stack.
            We treat the end of the list as the top of the stack.
    """

    stack_items: List[Any]

    def __init__(self) -> None:
        self.stack_items = []

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


class QueueList:
    """Creates a queue that uses python's default list as the underlying
    data structure.

    Attributes:
        queue_items (List[Any]): The list that stores the items in the queue.
            We treat the end of the list as the start of the queue and
            the start of the list as the end of the queue.
    """

    queue_items: List[Any]

    def __init__(self) -> None:
        self.queue_items = []

    def is_empty(self) -> bool:
        """Check if queue is empty.

        Returns:
            (bool): True if queue is empty, False otherwise.
        """
        return self.size == 0

    def enqueue(self, item: Any) -> None:
        """Insert an item at the end of the queue.

        In this implementation, the item is inserted at the start of the list.

        Args:
            item (Any): The current item to be queued.
        """
        self.queue_items.insert(0, item)

    def dequeue(self) -> Any:
        """Pop an item from the start of the queue.

        In this implementation, the item at the end of the list is returned and removed.
        We are using the list's pop method to do this.

        Raises:
            (Exception): If queue is empty.

        Returns:
            (Any): The item at the start of the queue.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.queue_items.pop()

    @property
    def size(self) -> int:
        """Return the size of the queue.

        Returns:
            (int): The size of the queue.
        """
        return len(self.queue_items)
