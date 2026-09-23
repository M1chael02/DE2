import time

def func():
    """My new function."""
    print("--- Hi there ---")

def triangle(lines):
    """Print a right-angled triangle of height 'lines'."""
    for row in range(1, lines + 1):
        print("*" * row)

def fibonacci(n):
    """Generate a list of the first n Fibonacci numbers."""
    start_time = time.ticks_us()  # Start timestamp in microseconds

    # TODO: Generate the first n Fibonacci numbers

    a, b = 0, 1

    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

    end_time = time.ticks_us()
    duration = end_time - start_time
    print()
    print(f"Execution time: {duration} us")

def factorial(n):
    """Return the factorial of a non-negative integer n."""
    # TODO: Implement factorial logic using a loop or recursion

    if (n == 1 or n==0):
        return 1

    else:
        return (n * factorial(n - 1))

    

# Run this only when executed directly, not when imported
if __name__ == "__main__":
    #func()
    #triangle(5)
    #fibonacci(10)

    print(f"5! = {factorial(5)}")  # Should print 120
    print(f"0! = {factorial(0)}")  # Should print 1