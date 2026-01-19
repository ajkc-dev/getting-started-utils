def add(a: float, b: float) -> float:
    """Adds two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The difference between a and b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiplies two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divides the first number by the second.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of the division.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


if __name__ == "__main__":
    try:
        x: float = 10.0
        y: float = 5.0
        z: float = 0.0

        print(f"{x} + {y} = {add(x, y)}")
        print(f"{x} - {y} = {subtract(x, y)}")
        print(f"{x} * {y} = {multiply(x, y)}")
        print(f"{x} / {y} = {divide(x, y)}")

        print(f"Attempting division by zero:")
        divide(x, z)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
