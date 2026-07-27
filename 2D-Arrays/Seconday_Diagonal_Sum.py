n, m = map(int, input().split())
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
sum=0
for i in range(n):
    sum+=arr[i][n-i-1]
print(sum)


# output
# 3 3
# 1 2 3
# 4 5 3
# 4 3 2
# 12
