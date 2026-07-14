# Last Occurrence
arr = [2, 2, 2, 4, 6]
target = 2
# Output = 2
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if target==arr[mid]:
            ans=mid
            low=mid+1
            
    elif target<arr[mid]:
        high=mid-1
    else:
        low=mid+1
        
print(ans)
