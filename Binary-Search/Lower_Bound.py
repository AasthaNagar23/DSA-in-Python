# Lower Bound
arr = [1, 2, 7, 2, 4, 6]
target = 9
# Output = 0
low=0
high=len(arr)-1
ans=len(arr)
while low<=high:
    mid=(low+high)//2
    count=0
    if target<=arr[mid]:
        ans=mid
        high=mid-1
    else:
        low=mid+1
        
print(ans)


# difference from the first occurance if only thant ki usme ans ki value hum -1 lete he but isme hum len(arr) lete he 