# jese jese stream aate ja rhi he means here it is arr ok vese vese we have to find the kth largest element 
import heapq
def kthlargest_stream(stream,k):
    arr=[]
    for i in stream:
        heapq.heappush(arr,i)
        if len(arr)>k:
            heapq.heappop(arr)
        if(len(arr)==k):   #yaha thoda dhyan dena it's not elif it's if
            print(arr[0])
        else:
            print("Not enough elements")
stream=[4,5,8,2]
k=3
kthlargest_stream(stream,k)