# Check if two arrays contain the same elements
s = "aastha"
s1 = "aastha"

freq = {}
freq1 = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for ch in s1:
    if ch in freq1:
        freq1[ch] += 1
    else:
        freq1[ch] = 1
        
equal=False  # yaha par ek baar equal print karne ke liye hamne false ka use kiye 

for ch in freq:
    if ch in freq1:
        if freq[ch] == freq1[ch]:
            equal=True
if equal==True:
    print("equal")
else:
    print("not equal")
    
    