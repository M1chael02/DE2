import time
import math

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
    fib_list = []

    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b

    end_time = time.ticks_us()
    duration = end_time - start_time
    print()
    print(f"Execution time: {duration} us")

    return fib_list

def factorial(n):
    """Return the factorial of a non-negative integer n."""
    # TODO: Implement factorial logic using a loop or recursion

    if (n == 1 or n==0):
        return 1

    else:
        return (n * factorial(n - 1))

def solve_quadratic(a, b, c):
    #solves equation using quadratic formula
    D = (b**2 - 4*a*c)

    if D > 0: 
        x1 = ((-b + math.sqrt(D)) / 2*a)
        x2 = ((-b - math.sqrt(D)) / 2*a)

        return (x1, x2)
        #print(f"x2 = {x2}")

    elif D == 0:
        x = (-b / 2*a)
        return x
        #print(f"x = {x}")

    else:
        return "No real solutions"

# Run this only when executed directly, not when imported
if __name__ == "__main__":
    #func()
    #triangle(5)
    #print(fibonacci(10))

    #print(f"5! = {factorial(5)}")  # Should print 120
    #print(f"0! = {factorial(0)}")  # Should print 1

    #print(solve_quadratic(1, -3, 2))  # Expected: (2.0, 1.0)
    #print(solve_quadratic(1, 2, 1))  # Expected: -1.0
    print(solve_quadratic(1, 1, 1))  # Expected: "No real solutions"