from itertools import permutations
arr=[1, 2, 1]
a=[]
p = permutations(arr)
for i in p:
    i=list(i)
    a.append(i)
print(a)
for i in range(len(a)-1):
    if a[i]==arr:
        print(a[i+1])
if a[-1]==arr:
    print(a[1])