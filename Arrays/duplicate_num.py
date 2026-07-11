arr=[1,2,4,3,2,3,2,33,7,6,2,9]
a=set(arr) #[1,2,4,3,33,7,6,9]
count=0
for i in arr:
    if i not in a:
        count+=1
