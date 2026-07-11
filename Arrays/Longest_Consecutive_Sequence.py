arr = list(map(int, input().split()))
arr.sort()
count=0
for i in range(len(arr)-1):
    if arr[i+1]==arr[i]+1:
        count+=1
print(count)