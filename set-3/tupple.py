def print_name_and_age(persons):
    for name, age in persons:
        print(f"{name} is {age} years old.")

# Test the function with the given list of tuples
persons = [("John", 25), ("Jane", 30)]
print_name_and_age(persons)
