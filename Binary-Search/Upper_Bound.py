# Upper Bound
arr = [1, 2, 2, 4, 6,7]
target =7
# Output = 
low=0
high=len(arr)-1
ans=len(arr)
while low<=high:
    mid=(low+high)//2
    if target<arr[mid]:    #sirf yaha par equals to nahi he as comparing to the lower bound
        ans=mid
        high=mid-1
    else:
        low=mid+1
        
print(ans)