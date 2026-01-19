def generate_fibonacci(n_terms: int) -> list[int]:
    """Generates a list containing the Fibonacci sequence up to the specified number of terms.

    Args:
        n_terms: The number of Fibonacci terms to generate. Must be a non-negative integer.

    Returns:
        A list of integers representing the Fibonacci sequence.
        Returns an empty list if n_terms is 0.
    """
    if n_terms < 0:
        raise ValueError("The number of terms must be a non-negative integer.")
    if n_terms == 0:
        return []
    if n_terms == 1:
        return [0]

    sequence: list[int] = [0, 1]
    while len(sequence) < n_terms:
        next_val: int = sequence[-1] + sequence[-2]
        sequence.append(next_val)

    return sequence


if __name__ == "__main__":
    try:
        num_terms = 10
        fib_sequence = generate_fibonacci(num_terms)
        print(f"Fibonacci sequence with {num_terms} terms: {fib_sequence}")
    except ValueError as e:
        print(f"Error: {e}")
