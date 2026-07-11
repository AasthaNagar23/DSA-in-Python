arr = [1,2,3,4]
c=[]


for i in range (len(arr)):
    m=1
    for j in range(len(arr)):
        if i!=j:
            m*=arr[j]
    c.append(m)
print(c)
