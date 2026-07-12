# First Non-Repeating Character
s="aastha"
for i in s:
    if s.count(i)==1:
        print(i)
        break
    #ek iteration ke baad break karne ke liye we use break