arr = [1, 2, -3, -4]
b=[]
for i in arr:
    if i>0:
        b.append(i)
        for i in arr:
            if i<0 and i not in b:
                b.append(i)
                break
print(b)