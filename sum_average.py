# Take 10 integers from user
numbers = []

print("Enter 10 integers:")
for i in range(10):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

# Calculate sum manually (without using sum())
total = 0
for n in numbers:
    total += n

# Calculate average
average = total / len(numbers)

# Print results
print("Numbers entered:", numbers)
print("Sum of numbers:", total)
print("Average of numbers:", average)
