# Count Occurrences
arr = [2, 2, 2, 4, 6]
target = 2
# Output = 0
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    count=0
    if target==arr[mid]:
            ans=mid
            count+=1
            low=mid+1  #left search karo and if it is equals to target +1 karo
            count+=1
            high=mid-1  #right side search karo if it is equal +1 karo
            count+=1
            
    elif target<arr[mid]:
        high=mid-1
    else:
        low=mid+1
        
print(count)
