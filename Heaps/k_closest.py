import heapq
def k_closest(points,k):
    arr=[]
    for x,y in points:
        distance=x*x+y*y
        heapq.heappush(arr,(-distance,[x,y]))  #here the array is storing dual things like distance and points 
        if len(arr)>k:
            heapq.heappop(arr)
    result = []
    for distance, point in arr:
        result.append(point)
    return result
    
points=[[1,3],[-2,2],[5,8]]
print(k_closest(points,2)) 