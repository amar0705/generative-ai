def initialize_dictionary(keys, defaults):
    result = {}

    for key in keys:
        result[key] = defaults

    return result

# Test the function with the given values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result_dict = initialize_dictionary(employees, defaults)
print(result_dict)
