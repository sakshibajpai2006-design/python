# Input a list from user
items = input("Enter elements separated by spaces: ").split()

# Reverse manually without reverse() or slicing
reversed_list = []
for i in range(len(items) - 1, -1, -1):
    reversed_list.append(items[i])

# Print results
print("Original list:", items)
print("Reversed list:", reversed_list)
