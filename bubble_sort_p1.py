def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Optimization: Track if any swap happened
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps, the list is already sorted
        if not swapped:
            break
    return arr
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr.copy())
print("Sorted Array:", sorted_arr)
