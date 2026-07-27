n, m = map(int, input().split())
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
sum=0
for i in range(n):
    sum+=arr[i][i]
print(sum)


# output
# 2 2
# 1 2
# 3 4
# 5