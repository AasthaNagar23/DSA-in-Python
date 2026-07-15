a=int(input("enter a number: "))
sum=0
for i in range(1,a,1):
    if (a%i==0):
        sum+=i
print("the summation of factors is: ",sum)
if sum==a:
    print("perfect number")
    