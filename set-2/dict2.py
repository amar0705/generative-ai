def extract_keys(dictionary, keys):
    result = {}

    for key in keys:
        if key in dictionary:
            result[key] = dictionary[key]

    return result

# Test the function with the given dictionary and keys
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"}

keys = ["name", "salary"]

result_dict = extract_keys(sample_dict, keys)
print(result_dict)
