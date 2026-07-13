# s = "abcabcbb"
# Possible substrings:
# abc length = 3
# abca 'a' repeats
# bca length = 3
# cab length = 3
s = "abcabcbb"
longest=0
for i in range(0,len(s)):
    a=""
    for j in range(i+1,len(s)):
        if s[j] not in a:
            a+=s[j]
        else:
            break
    if len(a) > longest:
        longest = len(a)
        print(longest)
    
        