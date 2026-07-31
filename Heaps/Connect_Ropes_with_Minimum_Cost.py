# Connect Ropes with Minimum Cost
import heapq
def CRMC(ropes):
    arr=ropes
    heapq.heapify(arr)
    cost=0
    while len(arr)>1:
        first=heapq.heappop(arr)
        second=heapq.heappop(arr)
        sum=first+second
        cost+=sum
        heapq.heappush(arr,sum)  #this means jo sum append honge uska bhi hame sum chahiye means use bhi hum add karke cost nikalenge ok  this is the main part of the code 
    return cost
ropes=[4,3,2,6]
print(CRMC(ropes))
