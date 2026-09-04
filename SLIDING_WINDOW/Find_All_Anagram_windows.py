# Find All Anagrams windows:
def find_anagram(s,p):
  ans=[]
  k=len(p)
  for i in range(len(s)-k+1):
    window=s[i:i+k]
    if sorted(window)==sorted(p):
      ans.append(window)

  return ans

s="cbaebabacd"
p= "abc"
print(find_anagram(s,p))
