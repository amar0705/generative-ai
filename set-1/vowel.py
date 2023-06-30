def count_vowels(input_string):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Initialize a counter for vowels
    vowel_count = 0

    # Iterate over each character in the string
    for char in input_string.lower():
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Test the function
input_str = "Hello"
vowel_count = count_vowels(input_str)
print("Number of vowels:", vowel_count)
