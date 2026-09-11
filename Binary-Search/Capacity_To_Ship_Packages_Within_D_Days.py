# Capacity To Ship Packages Within D Days:
# Ship ko D days ke andar saare packages deliver karne ke liye minimum kitni capacity (weight/day) rakhni padegi?
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
low=max(weights)
high=sum(weights)
while low<=high:
  capacity=(low+high)//2
  curr_weights=0
  req_days=1
  for i in weights:
    if i+curr_weights<=capacity:
      curr_weights+=i
    else:
      req_days+=1
      curr_weights=i
  if req_days<=days:
    high=capacity-1
  else:
    low=capacity+1
print(low)
