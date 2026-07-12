s="aabbaa"
half=len(s)//2
if len(s)%2==0:
    a=s[:half]
    b=s[half:]
    c=b[::-1]
    if a==c:
        print("palindrome")
    else:
        print("not plaindrome")
else:
    a=s[:half]
    b=s[half+1:]
    c=b[::-1]
    if a==c:
        print("palindrome")
    else:
        print("not plaindrome")