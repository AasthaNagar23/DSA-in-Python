n,m = map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(map(int, input().split())))
    
# Check Identity Matrix
identity=True
for i in range(n):
    for j in range(m):
        if i==j:
            if arr[i][j]!=1:
                identity=False
        else:
            if arr[i][j]!=0:
                identity=True
if identity==True:
    print("Identity Matrix")
else:
    print("Identity Matrix")