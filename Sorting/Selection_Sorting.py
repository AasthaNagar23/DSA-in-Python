#Selection  sort:
arr = [5,1,4,2]
for i in range(len(arr)-1):  # which position to fill 0,1,2,3...
    min_index=i
    for j in range(i+1,len(arr)):   # finding the min_value
        if arr[min_index]>arr[j]:
            min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)