n,m=map(int, input().split())
arr = []

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    
    
l = arr[0][0]
s = arr[0][0]
for i in range(n):
    for j in range(m):
        if arr[i][j]>l:
            l=arr[i][j]
        if arr[i][j]<s:
            s=arr[i][j]
print("Largest element: ",l)
print("Smallest element: ",s)