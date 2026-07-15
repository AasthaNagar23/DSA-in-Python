import math

n = int(input("Enter a number: "))
sum_fact = 0

while n > 0:
    digit = n % 10
    sum_fact += math.factorial(digit)
    n //= 10

if sum_fact == n:
    print("Strong Number")
else:
    print("Not a Strong Number")
   
