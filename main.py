"""CS202 Lab 1 - Sample Python Script for Pylint Workflow."""


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def factorial(n: int) -> int:
    """Compute factorial of n recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """Compute the nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def is_prime(num: int) -> bool:
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main() -> None:
    """Main function to run demo code."""
    print(greet("Luv"))

    print("\nFactorials:")
    for i in range(1, 6):
        print(i, "->", factorial(i))

    print("\nFibonacci Sequence:")
    for i in range(6):
        print(i, "->", fibonacci(i))

    print("\nPrime Check:")
    for i in range(2, 15):
        print(i, "->", is_prime(i))

    print("\nAddition Example:")
    print("2 + 3 =", add(2, 3))


if __name__ == "__main__":
    main()
