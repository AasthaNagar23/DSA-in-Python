arr = [0, 1, 2, 0, 3, 1, 4, 0]  #[1231400]
a=[]
b=[]

for i in arr:
    if i>0 or i<0:
        a.append(i)
    else:
        b.append(i)
c=a+b

print(c)




