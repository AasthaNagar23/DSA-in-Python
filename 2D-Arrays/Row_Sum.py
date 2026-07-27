n,m=map(int, input().split())
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    

for i in range(n):
    count=0
    for j in range(m):
        count+=arr[i][j]
    print("Row", i + 1, "Sum =", count)


# output
# 2 2
# 1 2
# 3 4
# Row 1 Sum = 3
# Row 2 Sum = 7