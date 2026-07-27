n,m = map(int,input().split())
arr=[]
arr1=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    arr1.append(list(map(int, input().split())))

result=[]
for i in range(n):
    row=[]
    for j in range(m):
        row.append(arr[i][j]+arr1[i][j])
    result.append(row)
    
for row in result:
    print(*row)
  