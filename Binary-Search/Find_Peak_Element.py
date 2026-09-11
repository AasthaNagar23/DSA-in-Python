# find peak element:
#means hame index nikalna he us element ka jo usse pehle and baad wale element se bada ho 
#arr[i] > arr[i-1]  AND  arr[i] > arr[i+1]
arr = [1, 2, 3, 1]
low=0
high=len(arr)-1
while low<high:  #yaha change he 
  mid=(low+high)//2
  if arr[mid]<arr[mid+1]:  #yaha bhi 
    low=mid+1
  else:
    high=mid  #yaha bhi 
print(low)
    