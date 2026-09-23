def factorial(n):
    """Return the factorial of n."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Test the function
num = int(input("Enter an integer: "))
print(f"Factorial of {num} is {factorial(num)}")
