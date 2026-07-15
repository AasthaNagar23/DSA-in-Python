# Fibonacci Series
n=6
first=0
second=1
a=[]
a.append(first)
a.append(second)
for i in range(2,n+1):
    i=first+second
    first=second
    second=i
    a.append(i)
print(a)
for i in a:
    print(i,end=" ")