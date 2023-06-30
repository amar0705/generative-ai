def add_name_age(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, age):
    if name in dictionary:
        dictionary[name] = age

def delete_name(dictionary, name):
    if name in dictionary:
        del dictionary[name]

# Test the functions with the given inputs
dictionary = {}

add_name_age(dictionary, "John", 25)
print(dictionary)

update_age(dictionary, "John", 26)
print(dictionary)

delete_name(dictionary, "John")
print(dictionary)
