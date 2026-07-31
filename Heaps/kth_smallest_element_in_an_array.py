import heapq
def kth_largest(arr,k): #this arr and arr1 ka dhyan rakhna they are different 
    arr1=[]
    for num in arr:
        heapq.heappush(arr1,-num)
        if len(arr1)>k:
            heapq.heappop(arr1)
    return -arr1[0]   #sirf minus ka difference he 
    
arr = [3,2,1,5,6,4]
print(kth_largest(arr,2))

# isme hum max heap ke sath khelte he 