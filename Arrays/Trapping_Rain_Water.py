arr = [0,1,0,2,1,0,1,3,2,1,2,1]

total = 0

for i in range(len(arr)):
    
    left_max = max(arr[:i+1])
    right_max = max(arr[i:])
    
    water = min(left_max, right_max) - arr[i]
    
    total += water

print(total)