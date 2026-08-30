# sliding window:
s=input()
left=0
vowel_count=0
longest=""
vowels="aeiouAEIOU"
for right in range(len(s)):
    if s[right] in vowels: #right se element add ho rhe he 
        vowel_count+=1     #vowel_count add hoga but
    while vowel_count>2:
        if s[left] in vowels:   
#jese jese hum window slide karenge left se shrink kkarenge na to is left vowel he then vowel_count kam hota jaega samjhe 
            vowel_count-=1
        left+=1
    if vowel_count==2:
        current=s[left:right+1]
        if len(current)>len(longest):
            longest=current
print(longest)