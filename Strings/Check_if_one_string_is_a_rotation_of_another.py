# Check if one string is a rotation of another
s=input()
s1=input()
if len(s)==len(s1) and s1 in s+s1:
    print("rotation")
else:
    print("not rotation")