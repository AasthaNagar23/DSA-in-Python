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
        print(i,"->",freq[i],"max values")
    if freq[i]==min(freq.values()):
        print(i,"->",freq[i],"min values")
        # here we have use the new operation that is max and min

        
    # output
    # a -> 3 max values
    # s -> 1 min values
    # t -> 1 min values
    # h -> 1 min values
    
     