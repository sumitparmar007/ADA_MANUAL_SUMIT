def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        # Find the minimum element in the unsorted part
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap if a smaller element was found
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [29, 10, 14, 37, 14]
sorted_arr = selection_sort(arr.copy())
print("Sorted Array:", sorted_arr)
