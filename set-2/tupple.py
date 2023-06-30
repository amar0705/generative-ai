# Given nested tuple
tuple1 = (11, [22, 33], 44, 55)

# Convert the tuple to a list to modify the nested list item
modified_list = list(tuple1)

# Modify the first item (22) of the nested list to 222
modified_list[1][0] = 222

# Convert the modified list back to a tuple
modified_tuple = tuple(modified_list)

# Print the modified tuple
print(modified_tuple)
