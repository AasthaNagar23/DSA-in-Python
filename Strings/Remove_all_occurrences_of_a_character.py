# Remove all occurrences of a character
s=input()
target="a"
a=""
for i in s:
    if i!=target:
        a+=i
print(a)