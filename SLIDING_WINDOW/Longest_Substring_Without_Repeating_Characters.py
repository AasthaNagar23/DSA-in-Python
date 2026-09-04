s="abcabcbb"
# longest substring without repeating characters:
def long_subs(s):
  max_len=0
  left=0
  seen=set()
  for right in range(len(s)):
    while s[right] in seen:
      #left wala delete kar rhe he and right wala add kar rhe he:
      seen.remove(s[left])  
      left+=1
    #else:
    seen.add(s[right])
    max_len=max(max_len,right-left+1)
  return max_len
print(long_subs(s))