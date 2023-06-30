def append_middle(s1, s2):
    middle_index = len(s1) // 2  # Find the middle index of s1
    s3 = s1[:middle_index] + s2 + s1[middle_index:]  # Concatenate s2 in the middle of s1
    return s3

# Test the function with the given strings
s1 = "Ault"
s2 = "Kelly"
s3 = append_middle(s1, s2)
print(s3)
