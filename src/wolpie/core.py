def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers together.

    :param int | float a: First number to add
    :param int | float b: Second number to add
    :return int | float: Sum of the two numbers
    """
    return a + b


def multiply(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers.

    :param int | float a: First number to multiply
    :param int | float b: Second number to multiply
    :return int | float: Product of the two numbers
    """
    return a * b


def divide(a: int | float, b: int | float) -> float:
    """Divide first number by second number.

    :param int | float a: Dividend (number to be divided)
    :param int | float b: Divisor (number to divide by)
    :raises ValueError: If divisor is zero
    :return float: Result of division
    """
    if b == 0:
        msg = "Cannot divide by zero"
        raise ValueError(msg)
    return a / b
