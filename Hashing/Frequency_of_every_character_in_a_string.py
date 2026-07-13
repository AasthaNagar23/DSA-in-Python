# Frequency of every character in a string
s="aastha"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for i in freq:
    print(i,"->",freq[i])   

    # output:
    # a -> 3
    # s -> 1
    # t -> 1
    # h -> 1