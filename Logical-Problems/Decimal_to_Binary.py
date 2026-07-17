# Decimal to Binary
a=12
c=[]
d=0
while a>0:
    b=a%10
    b=a%2
    a//=2
    c.append(b)
print(c)
c.reverse()
print(c)
