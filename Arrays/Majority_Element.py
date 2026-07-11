arr = [2,2,1,1,1,2,1]

n = len(arr)

for i in range(n):
    count = 0

    for j in range(n):
        if arr[i] == arr[j]:
            count += 1

    if count > n // 2:
        print("Majority Element:", arr[i])
        break