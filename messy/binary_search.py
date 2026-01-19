from typing import List, Optional

def binary_search(sorted_list: List[int], target: int) -> int:
    """Performs binary search on a sorted list of integers.

    Args:
        sorted_list: A list of integers sorted in ascending order.
        target: The integer to search for.

    Returns:
        The index of the target element if found, otherwise -1.
    """
    left: int = 0
    right: int = len(sorted_list) - 1

    while left <= right:
        mid: int = (left + right) // 2
        mid_val: int = sorted_list[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    # Test cases
    test_list: List[int] = [1, 3, 5, 7, 9, 11, 13, 15]
    
    # Case 1: Target exists
    target_val: int = 7
    result_index: int = binary_search(test_list, target_val)
    if result_index != -1:
        print(f"Found {target_val} at index {result_index}.")
    else:
        print(f"{target_val} not found in the list.")

    # Case 2: Target does not exist
    target_val_not_found: int = 6
    result_index_nf: int = binary_search(test_list, target_val_not_found)
    if result_index_nf != -1:
        print(f"Found {target_val_not_found} at index {result_index_nf}.")
    else:
        print(f"{target_val_not_found} not found in the list.")
