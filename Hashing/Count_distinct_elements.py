# count distict elements:
s="aastha"
freq={}
count=0
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for i in freq:
    count+=1
print(len(freq))  