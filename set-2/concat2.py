def concatenate_lists(list1, list2):
    result = []

    for item1 in list1:
        for item2 in list2:
            concatenated_item = item1 + item2
            result.append(concatenated_item)

    return result

# Test the function with the given lists
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result_list = concatenate_lists(list1, list2)
print(result_list)
