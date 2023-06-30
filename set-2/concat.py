def concatenate_lists(list1, list2):
    result = []

    # Determine the length of the shorter list
    min_length = min(len(list1), len(list2))

    # Concatenate items index-wise
    for i in range(min_length):
        concatenated_item = list1[i] + list2[i]
        result.append(concatenated_item)

    # Add any leftover items from the longer list
    if len(list1) > min_length:
        result.extend(list1[min_length:])
    elif len(list2) > min_length:
        result.extend(list2[min_length:])

    return result

# Test the function with the given lists
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result_list = concatenate_lists(list1, list2)
print(result_list)
