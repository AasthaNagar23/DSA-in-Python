a=int(input("enter a number: "))
print(a)
if str(a) == str(a)[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
