# Find the highest frequency element
s="aastha"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for i in freq:
    if freq[i]==max(freq.values()):
        print(i,"->",freq[i])
        # here we have use the new operation that is max 