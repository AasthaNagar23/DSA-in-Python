n,m = map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(map(int, input().split())))
    
# Rotate Matrix 90°: transpose+reverse the digits in each row
t=[]
for j in range(m):
    row=[]
    for i in range(n):
        row.append(arr[i][j])
        
    t.append(row)
for i in range(len(t)):
    t[i].reverse()
for i in t:
    print(*i)


# output
# 3 3
# 1 2 3
# 3 4 5
# 6 7 8
# 6 3 1
# 7 4 2
# 8 5 3