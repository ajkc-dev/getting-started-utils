import random
import time
from typing import List

def optimized_sort(data: List[int]) -> List[int]:
    """Sorts a list of integers using Python's highly optimized Timsort.

    Time Complexity: O(n log n) - Timsort is a hybrid sorting algorithm, 
    derived from merge sort and insertion sort.
    
    Args:
        data: The list of integers to sort.

    Returns:
        The sorted list.
    """
    # Create a copy to avoid mutating the original list in place if that's desired
    sorted_data = sorted(data)
    return sorted_data

def benchmark_sort(data: List[int]) -> None:
    """Benchmarks the optimized sorting operation.

    Args:
        data: The list of integers to process.
    """
    n = len(data)
    print(f"Starting optimized sort on {n} elements...")
    start_time = time.time()

    # Python's built-in sort is extremely fast and efficient
    result = optimized_sort(data)

    end_time = time.time()
    print(f"Finished.")
    print(f"Time taken: {end_time - start_time:.6f} seconds")
    
    # Verify correctness
    assert result == sorted(data), "Sort failed!"
    print("Verification: Sort successful.")

if __name__ == "__main__":
    # Generate a random list of integers
    # Increased size significantly to demonstrate efficiency
    sample_data = [random.randint(1, 10000) for _ in range(100000)]
    
    print(f"Original Data Size: {len(sample_data)}")
    benchmark_sort(sample_data)
