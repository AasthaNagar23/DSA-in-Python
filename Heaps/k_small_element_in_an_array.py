import heapq
def kth_largest(arr,k): #this arr and arr1 ka dhyan rakhna they are different 
    arr1=[]
    for num in arr:
        heapq.heappush(arr1,-num)
        if len(arr1)>k:
            heapq.heappop(arr1)
    return [-x for x in arr1]   #this is also impportant as isme [-2,-1] se [2,1 ] ese la sakte he hum 
    
arr = [3,2,1,5,6,4]
print(kth_largest(arr,2))