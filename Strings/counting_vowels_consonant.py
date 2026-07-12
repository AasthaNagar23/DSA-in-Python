s="aasthanagar"
vowels=0
consonants=0
for ch in s:
    if ch=="a" or ch=="e" or ch=="i" or ch=="o"or ch=="u":
        vowels+=1
    else:
        consonants+=1
print(vowels,consonants)