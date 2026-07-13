# Longest Common Prefix
a="flower"
b="flew"
c="float"
d=0
e=[]
for i in range(0,len(a)):
    for j in range(0,len(b)):
        for k in range(0,len(c)):
            if a[i]==b[j]==c[k]:
                e.append(a[i])
print(e)
f="".join(e)
print(f)



# Longest Common Prefix
# solution 2nd
a="flower"
b="flew"
c="float"
d=0
e=[]
for i in range(0,len(b)):
    if a[i] in b[i]:
        if a[i] in c[i]:
            e.append(a[i])
print(e)
f="".join(e)
print(f)