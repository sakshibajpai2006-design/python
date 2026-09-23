def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test the function
c = float(input("Enter temperature in Celsius: "))
f = celsius_to_fahrenheit(c)
print(f"Temperature in Fahrenheit is: {f}")
