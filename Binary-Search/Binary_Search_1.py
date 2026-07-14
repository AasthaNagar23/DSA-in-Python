# binary search only work on th sorted arrays
# here we use the two pointer that are low=0 and high=len(arr)-1
# and mid pointer that is mid=(low+high)//2
# Binary Search
# with this we can reduce time complexity of the code by not using the for loop 
arr = [1, 3, 3, 4, 5, 7, 9]
target = 3
# Output = 2
low=0
high=len(arr)-1
while low<=high:  #very very important condition for the ninary search
    mid=(low+high)//2
    if target== arr[mid]:
        print(mid)
        break
    elif target<arr[mid]:
        high=mid-1
    else:
        low=mid+1 

        
# break isiliye use kiya to break the while loop 
            

    
