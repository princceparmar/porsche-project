"""
utils.py
A small standalone command-line utility for basic number analysis.
Not connected to the Porsche website — safe to keep in the same repo.

Run it directly:
    python utils.py
"""

def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci_series(count: int) -> list:
    """Return the first `count` numbers of the Fibonacci sequence."""
    series = []
    a, b = 0, 1
    for _ in range(count):
        series.append(a)
        a, b = b, a + b
    return series


def factorial(n: int) -> int:
    """Return n! (n factorial)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def reverse_string(text: str) -> str:
    """Return the reversed version of a string."""
    return text[::-1]


def main():
    print("=== Number & String Utility Demo ===\n")

    n = 29
    print(f"Is {n} prime? {is_prime(n)}")

    count = 10
    print(f"First {count} Fibonacci numbers: {fibonacci_series(count)}")

    fact_n = 6
    print(f"{fact_n}! = {factorial(fact_n)}")

    sample_text = "Engineering"
    print(f"Reversed '{sample_text}': {reverse_string(sample_text)}")


if __name__ == "__main__":
    main()
