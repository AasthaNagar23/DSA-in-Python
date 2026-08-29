# Count frequency of each word
s=input()
d={}
a=s.split()
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    print(i,d[i])