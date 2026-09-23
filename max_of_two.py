def find_maximum(a, b):
    """Return the greater of two numbers."""
    if a > b:
        return a
    else:
        return b

# Test the function
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = find_maximum(num1, num2)
print("The greater number is:", result)
