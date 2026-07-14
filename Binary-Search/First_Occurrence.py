# First Occurrence
arr = [2, 2, 2, 4, 6]
target = 2
# Output = 0
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid=(low+high)//2
    if target==arr[mid]:
            ans=mid   #kisi mein save karo mid and then high ko change karo to search in the lower vound
            high=mid-1
            
    elif target<arr[mid]:
        high=mid-1
    else:
        low=mid+1
        
print(ans)

# arr[mid] == target first occurance mein ye condition thi ki pehle hum equal sto check karte he then kaam karte he 
# but in the lower bound we check for the lower bound that is <=arr[mid] then hum dono conditions likh dennge 


        
