n,m = map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(map(int, input().split())))
    
# Check Symmetric Matrix

symmetric=True
for i in range(n):
    for j in range(m):
        if arr[i][j]!=arr[j][i]:
            symmetric=False
            break
if symmetric==True:
    print("Symmetric")
else:
    print("not symmetric")