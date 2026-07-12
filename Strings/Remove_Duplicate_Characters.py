# ek baar dekh lena 
# Remove Duplicate Characters
# different logic of the strings
s="aas^6^stha"
s1=""
for i in s:
    if i not in s1:
        s1+=i
print(s1)
            