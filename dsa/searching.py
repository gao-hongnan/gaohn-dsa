from __future__ import annotations

import math
from typing import Iterable, TypeVar, Tuple

T = TypeVar("T", str, int, float)  # T should be of type int, float or str


def unordered_sequential_search_iterative(
    container: Iterable[T], target: T
) -> Tuple[bool, int]:
    """If the target element is found in the container, returns True and its index,
    else, return False and -1 to indicate the not found index."""
    is_found = False  # a flag to indicate so your return is more meaningful
    index = 0
    for item in container:
        if item == target:
            is_found = True
            return is_found, index
        index += 1
    return is_found, -1


def unordered_sequential_search_recursive(
    container: Iterable[T], target: T, index: int = 0
) -> int:
    """Recursive implementation of unordered Sequential Search."""
    if len(container) == 0:  # if not container is also fine
        return -1  # not found

    if container[0] == target:  # this is base case
        return index  # found

    # notice we increment index by 1 to mean index += 1 in the iterative case
    return unordered_sequential_search_recursive(
        container[1:], target, index + 1
    )  # recursive case


def ordered_sequential_search(container: Iterable[T], target: T) -> Tuple[bool, int]:
    """Sequential search for ordered container."""
    is_found = False  # a flag to indicate so your return is more meaningful
    index = 0
    for item in container:
        if item == target:
            is_found = True
            return is_found, index
        index += 1
        if item > target:
            return is_found, -1
    # do not forget this if not if target > largest element in container, this case is not covered
    return is_found, -1


def binary_search_iterative(
    container: Iterable[T], target: T, left_index: int, right_index: int
) -> int:
    """Binary search iterative implementation."""
    while left_index <= right_index:
        # (left_index + right_index) // 2 will cause overflow.
        mid_index = left_index + math.floor((right_index - left_index) / 2)

        # Check if target is present at mid
        if container[mid_index] == target:
            return mid_index

        # If target is greater, we discard left half, so we update left_index
        elif container[mid_index] < target:
            left_index = mid_index + 1

        # If target is smaller, we discard right half, so we update right_index
        else:
            right_index = mid_index - 1

    # Search has ended and target is not present in the container
    return -1


def binary_search_recursive(
    container: Iterable[T], target: T, left_index: int, right_index: int
) -> int:
    """Binary search recursive implementation."""
    mid_index = left_index + math.floor((right_index - left_index) / 2)
    if left_index <= right_index:
        if container[mid_index] == target:
            return mid_index  # base case 1
        elif container[mid_index] < target:
            return binary_search_recursive(
                container, target, mid_index + 1, right_index
            )
        else:
            return binary_search_recursive(container, target, left_index, mid_index - 1)
    else:
        return -1  # base case 2


if __name__ == "__main__":
    ordered_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    left_index = 0
    right_index = len(ordered_list) - 1
    print(binary_search_iterative(ordered_list, -1, left_index, right_index))
    print(binary_search_iterative(ordered_list, 3.5, left_index, right_index))
    print(binary_search_iterative(ordered_list, 42, left_index, right_index))
    print(binary_search_recursive(ordered_list, -1, left_index, right_index))
    print(binary_search_recursive(ordered_list, 3.5, left_index, right_index))
    print(binary_search_recursive(ordered_list, 42, left_index, right_index))
