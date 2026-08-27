strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
result=[]
for i in strs:
    found=False #har ek ke liye pehle false hoga then if true hoga to arr mein append ho jaega
    for arr in result:
        if sorted(i)==sorted(arr[0]):
            arr.append(i)
            found=True
    if found==False:
        result.append([i])
print(result)
 