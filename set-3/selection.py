def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the minimum element with the first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

# Test the function with the given input
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)
