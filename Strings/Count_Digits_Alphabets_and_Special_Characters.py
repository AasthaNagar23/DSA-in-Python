s="aasthana26455792846#$^*%@gar"
alphabets=0
digits=0
special=0
for ch in s:
    if ch.isalpha():
        alphabets+=1
    elif ch.isdigit():
        digits+=1
    else:
        special+=1
print(alphabets,digits,special)
    