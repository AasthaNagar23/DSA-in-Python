n,m=map(int, input().split())
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    

for j in range(m):
    count=0
    for i in range(n):
        count+=arr[i][j]
    print("Column", j + 1, "Sum =", count)