s = "abciiidef"
vowels="aeiouAEIOU"
k = 3
left=0
count=0
max_s=0
for right in range(len(s)):
    if s[right] in vowels:
        count+=1
    if right-left+1==k:
        max_s=max(max_s,count)
        if s[left] in vowels:
            count-=1
        left+=1
print(max_s)
    
