# Longest word in a sentence
s=input()
a=s.split()
max=0
for i in a:
    if max<len(i):
        max=len(i)
for i in a:
    if len(i)==max:
        print(i)