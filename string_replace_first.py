def change_string(s):
    """Try to replace the first character of the string with 'X'."""
    if s:  # check if string is not empty
        # Strings are immutable, so we must create a new one
        new_s = "X" + s[1:]
        return new_s
    return s

# Test the function
original_str = "hello"
print("Original string before function call:", original_str)

modified_str = change_string(original_str)

print("String returned from function:", modified_str)
print("Original string after function call:", original_str)
