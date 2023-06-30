def arrange_characters(str1):
    lowercase = ""
    uppercase = ""
    
    for char in str1:
        if char.islower():
            lowercase += char
        else:
            uppercase += char
    
    arranged_str = lowercase + uppercase
    return arranged_str

# Test the function with the given string
str1 = "PyNaTive"
arranged_str = arrange_characters(str1)
print(arranged_str)
