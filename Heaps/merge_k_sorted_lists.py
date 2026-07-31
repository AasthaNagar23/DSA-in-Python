import heapq
def merge_k_lists(lists):
    arr=[]
    for i in range(len(lists)):
        if list[i]:
            heapq.heappush(arr,lists[i][0])  #iska matlab we hae to push the list ith smallest element in the arr
    result=[]
    while arr:
        smallest=heapq.heappop(arr)
        result.append(smallest)
    return result
lists = [[1,4,5],[1,3,4],[2,6]]
print(merge_k_lists(lists))

# [1,1,2]