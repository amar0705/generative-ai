def is_palindrome(word):
    word = word.lower()  # Convert the word to lowercase
    reversed_word = word[::-1]  # Reverse the word
    
    if word == reversed_word:
        return True
    else:
        return False

# Test the function with the given input
word = "madam"

if is_palindrome(word):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")
