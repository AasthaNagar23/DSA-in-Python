def merge_sort(arr):

    # Base case: If the array has 0 or 1 element,
    # it is already sorted.
    if len(arr) <= 1:
        return arr

    # Find the middle index
    mid = len(arr) // 2

    # Divide the array into left and right halves
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the two sorted halves
    return merge(left, right)


def merge(left, right):

    result = []      # Stores the merged sorted array
    i = 0            # Pointer for left array
    j = 0            # Pointer for right array

    # Compare elements from both arrays
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            result.append(left[i])   # Add smaller element
            i += 1                   # Move left pointer
        else:
            result.append(right[j])  # Add smaller element
            j += 1                   # Move right pointer

    # Add remaining elements of left array
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add remaining elements of right array
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


arr = [8, 3, 5, 4]

sorted_array = merge_sort(arr)

print(sorted_array)