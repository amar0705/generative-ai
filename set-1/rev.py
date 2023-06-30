def reverse_string(input_string):
    # Using slicing to reverse the string
    reversed_string = input_string[::-1]
    return reversed_string

# Test the function
input_str = "Python"
reversed_str = reverse_string(input_str)
print(reversed_str)
