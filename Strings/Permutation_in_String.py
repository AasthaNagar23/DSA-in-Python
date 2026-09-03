from itertools import permutations
s1 = "ab"
s2 = "eidbaooo"
a=[]
arr=[]
for i in s1:
    a.append(i)
p=permutations(a)
for i in p:
    i=list(i)
    m="".join(i)
    arr.append(m)
print(arr)
found=False
for i in arr:
    if i in s2:
        found=True
        break
    else:
        found=False
print(found)