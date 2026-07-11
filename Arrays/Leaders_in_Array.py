# element is called a leader if it is greater than or equal to all the elements to its right side.
# we will hae to print all the elements that are leaders 
arr = [16, 17, 4, 3, 5, 2]
leader=arr[len(arr)-1]
c=[leader]
l=len(arr)-2
while len(arr)==0:
    for i in range(len(arr-2),-1,-1):
        if arr[i]>arr[leader]:
            leader=arr[i]
    c.append(leader)
    print(c)





