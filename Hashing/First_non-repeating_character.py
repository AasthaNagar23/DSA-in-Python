# First non-repeating character
s="aastha"
freq={}
count=0
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for i in freq:
    if freq[i]==1:
        print(i)
        break