from typing import List, Any


class QueueList:
    """Creates a queue that uses python's default list as the underlying
    data structure.

    Attributes:
        queue_items (List[Any]): The list that stores the items in the queue.
            We treat the end of the list as the start of the queue and
            the start of the list as the end of the queue.
    """

    _queue_items: List[Any]

    def __init__(self) -> None:
        self._queue_items = []

    @property
    def queue_items(self) -> List[Any]:
        """Read only property for the queue items."""
        return self._queue_items

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


class DeQueueList:
    """Creates a double-ended queue that uses python's default list as the underlying
    data structure.

    Attributes:
        queue_items (List[Any]): The list that stores the items in the queue.
            We treat the end of the list as the start of the queue and
            the start of the list as the end of the queue.
    """

    _queue_items: List[Any]

    def __init__(self) -> None:
        self._queue_items = []

    @property
    def queue_items(self) -> List[Any]:
        """Read only property for the queue items."""
        return self._queue_items

    def is_empty(self) -> bool:
        """Check if queue is empty.

        Returns:
            (bool): True if queue is empty, False otherwise.
        """
        return self.size == 0

    def add_front(self, item: Any) -> None:
        """Insert an item at the front of the queue.

        Args:
            item (Any): The current item to be added.
        """
        self.queue_items.append(item)

    def add_rear(self, item: Any) -> None:
        """Insert an item at the end of the queue.

        In this implementation, the item is inserted at the start of the list.

        Args:
            item (Any): The current item to be queued.
        """
        self.queue_items.insert(0, item)

    def remove_front(self) -> Any:
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

    def remove_rear(self) -> Any:
        """Pop an item from the end of the queue.

        Raises:
            (Exception): If queue is empty.

        Returns:
            (Any): The item at the end of the queue.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.queue_items.pop(0)

    @property
    def size(self) -> int:
        """Return the size of the queue.

        Returns:
            (int): The size of the queue.
        """
        return len(self.queue_items)
