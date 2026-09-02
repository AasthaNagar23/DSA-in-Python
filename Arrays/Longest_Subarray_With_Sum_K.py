arr = [10, 5, 2, 7, 1, 9]
k = 15
max_len=0
for i in range(len(arr)):
    count=0
    sum=0
    for j in range(i,len(arr)):
        sum+=arr[j]
        count+=1
        if sum==k:
            max_len=max(count,max_len)
print(max_len)
 