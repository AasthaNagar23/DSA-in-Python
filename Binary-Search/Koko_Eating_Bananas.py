# Koko Eating Bananas:
#Koko ko h hours ke andar saare bananas khatam karne ke liye minimum kitni bananas/hour ki speed rakhni padegi?
piles = [3, 6, 7, 11]
h = 8
low=0
high=max(piles)   #yaha difference he 
while low<=high:
  mid=(low+high)//2
  hours=0
  for i in piles:    #yaha bhi
    hours+=(i+mid-1)//mid
  if hours<=h:
    high=mid-1
  else:
    low=mid+1
print(low)