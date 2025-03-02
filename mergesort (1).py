def merge_sort(array):
    if len(array) <= 1:
        return array

    # Splitting the array into halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursively sorting each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merging the sorted halves
    sorted_array = merge(sorted_left, sorted_right)
    print(f"Merging {sorted_left} and {sorted_right} into {sorted_array}")
    return sorted_array

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements from both halves and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Input list
input_list = [7, 2, 5, 6, 3, 1, 8, 4]
print(f"Input List: {input_list}")

# Perform Merge Sort
sorted_list = merge_sort(input_list)

# Output the final sorted list
print(f"Sorted List: {sorted_list}")
