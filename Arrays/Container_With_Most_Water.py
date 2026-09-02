arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
area = 0

for left in range(len(arr)):
    for right in range(left + 1, len(arr)):
        if area < min(arr[left], arr[right]) * (right - left):
            area = min(arr[left], arr[right]) * (right - left)

print(area)