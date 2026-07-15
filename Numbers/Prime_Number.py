# Check Prime Number
a=int(input())
b=[]
for i in range(2,a):
    if a%i==0:
        b.append(i)
if len(b)==0 and a>1:
    print("prime")
else:
    print("not prime")
    print("factors: ",b)

# output: 
# 8
# not prime
# factors:  [2, 4]