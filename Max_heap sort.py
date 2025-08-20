def heapify(arr, n, i):
    largest = i          # Initialize largest as root
    left = 2 * i + 1     # left child index
    right = 2 * i + 2    # right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Heapify the affected subtree recursively
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # call max heapify on reduced heap
        heapify(arr, i, 0)

    return arr
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr.copy())
print("Sorted array is:", sorted_arr)
