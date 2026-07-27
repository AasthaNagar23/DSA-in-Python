n,m = map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(map(int, input().split())))
    
# Search an Element:
target=4
found=False
for i in range(n):
    for j in range(m):
        if arr[i][j]==target:
            print(i,j)
            found=True
if found==True:
    print("in the matrix")
else:
    print("not in the matrix")