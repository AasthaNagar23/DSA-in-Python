# Print Prime Numbers in Range
a=int(input())
c=int(input())
b=[]
d=0
e=[]
for i in range(a,c+1):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            b.append(i)
for i in b:
    if i not in e:
        e.append(i)
print(e)
