def add_entry(d, key, value):
    """Add a new key-value pair into the dictionary."""
    d[key] = value

def reassign_dict(d):
    """Reassign the dictionary variable to a new dictionary."""
    d = {"new_key": "new_value"}
    return d

# Test the functions
my_dict = {"a": 1, "b": 2}
print("Original dictionary before function calls:", my_dict)

# Add entry modifies the original dictionary
add_entry(my_dict, "c", 3)
print("Dictionary after add_entry:", my_dict)

# Reassign_dict does not change the original dictionary outside the function
new_dict = reassign_dict(my_dict)
print("Dictionary returned from reassign_dict:", new_dict)
print("Original dictionary after reassign_dict:", my_dict)
