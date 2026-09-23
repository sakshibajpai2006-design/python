def remove_last(lst):
    """Removes the last element of the list."""
    if lst:  # check if list is not empty
        lst.pop()

# Test the function
my_list = [10, 20, 30, 40]
print("Original list before function call:", my_list)

remove_last(my_list)

print("List after function call:", my_list)
