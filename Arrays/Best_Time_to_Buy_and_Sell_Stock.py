arr=[7,1,5,3,6,4]
a=min(arr)
print("buying at", a)
buy=a
c=arr[buy]
f=[]
for i in range(c+1,len(arr)):
    d=arr[i]-buy
    f.append(d)

for i in range(c):
    e=arr[i]-buy
    f.append(e)
g=max(f)
print("maximum profit: ",g)


