arr = [-2,1,-3,4,-1,2,1,-5,4]
curr_max = arr[0]
curr_min = arr[0]
max_prod = arr[0]
for i in range(1, len(arr)):
    temp = curr_max
    curr_max = max(arr[i], arr[i] * temp, arr[i] * curr_min)
    curr_min = min(arr[i], arr[i] * temp, arr[i] * curr_min)
    max_prod = max(max_prod, curr_max)
print(max_prod)