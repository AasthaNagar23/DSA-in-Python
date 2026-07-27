# when n and m are equal 
n,m = map(int,input().split())
arr=[]
arr1=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    arr1.append(list(map(int, input().split())))

# Matrix Multiplication
result=[]
for i in range(n):
    row=[]
    for j in range(m):
        s=0
        for k in range(m):
            s+=(arr[i][j]*arr[j][i])
        row.append(s)
    result.append(row)
for i in result:
    print(*i)



# if n and m are not equal:
n, m = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

n2, m2 = map(int, input().split())
arr1 = []

for i in range(n2):
    arr1.append(list(map(int, input().split())))

if m != n2:
    print("Matrix multiplication not possible")
else:
    result = []

    for i in range(n):
        row = []
        for j in range(m2):
            s = 0
            for k in range(m):
                s += arr[i][k] * arr1[k][j]
            row.append(s)
        result.append(row)

    for row in result:
        print(*row)
