def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        print(f"Heapified subtree with root at index {i}: {arr}")
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        print(f"Max heap after heapifying index {i}: {arr}")

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        print(f"Swapped max element with last element: {arr}")
        heapify(arr, i, 0)

input_list = [7, 2, 5, 6, 3, 1, 8, 4]
print(f"Original list: {input_list}")
heap_sort(input_list)
print(f"Sorted list: {input_list}")
