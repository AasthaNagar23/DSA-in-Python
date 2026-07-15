n=int(input("enter a number: "))
print(n)
digits=len(str(n))
sum=0
temp=n

while temp>0:
    a=temp%10
    sum+=(a**digits)
    temp//=10

if (sum==n):
    print("The number is an armstrong number.")
else:
    print("The number is not an armstrong number.")

