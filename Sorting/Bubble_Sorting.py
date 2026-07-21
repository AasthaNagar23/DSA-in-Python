#Bubble sort:
arr = [5,1,4,2]
for i in range(len(arr)-1):  #number of passes 
    for j in range(len(arr)-i-1):   #used for comparision
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)