arr = list(map(int, input().split()))
k=int(input())
found= False 
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]-arr[j]==k:
            found = True
            break
        if found:
            break
if found == True:
    print("true")
else:
    print("false")

            
        

