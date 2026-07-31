# Last Stone Weight:
# isme hum baar baar max element dhund rahe he therefore max heap
# here the main idea is that smalllest positive largest negative
import heapq
def lsw(stones):
    arr=[]
    for num in stones:
        heapq.heappush(arr,-num)   #max heap
    while len(arr)>1:
        first=(-heapq.heappop(arr))   #jab nikalna ho then we have to use the negative sign ok 
        second=(-heapq.heappop(arr))
        if first!=second:
            remaining=first-second
            heapq.heappush(arr,-remaining)
    if arr:
        return -arr[0]
    return 0
stones= [2,7,4,1,8,1]
print(lsw(stones))
  