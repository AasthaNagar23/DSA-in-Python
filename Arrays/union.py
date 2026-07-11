a=[1,2,3,4,5]
b=[2,3,4,8,7,9]
c=[]
for i in a:
    c.append(i)
for i in b:   # the mistake i was doing is in this hum i ko c par iterate kar rhe he to changes c mein nahi honge
    if i not in c:
        c.append(i)
print(c)
