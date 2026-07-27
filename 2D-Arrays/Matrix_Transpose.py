n, m = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
for j in range(m):
    for i in range(n):
        print(arr[i][j],end=" ")
    print()


# output: 
# 3 4
# 1 2 3 4
# 2 3 4 5
# 2 3 4 5
# 1 2 2 
# 2 3 3 
# 3 4 4 
# 4 5 5 
