#1st method
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c=a
a=b
b=c
print("After swapping: a =", a, "b =", b)

#2nd method
a=12
b=13
a=a+b   #25 a
b=a-b   #12 b
a=a-b   #13 a
print(a)
print(b)