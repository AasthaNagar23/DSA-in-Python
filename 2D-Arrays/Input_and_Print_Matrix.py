n = int(input())
m = int(input())

arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(n):
    for j in range(m):
        print(arr[i][j],end=" ")
    print()