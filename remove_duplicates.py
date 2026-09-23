# Input integers into a list
numbers = list(map(int , input("Enter integers seprated by spaces: ").split()))
# Remove duplicates while preserving the order
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        # Display the result ( outside the loop to avoid printing multiple times)
        print("Original list:", numbers)
        print("List after removing duplicates:", unique_numbers)
