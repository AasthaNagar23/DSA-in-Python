arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]    #[4, -1, 2, 1] final output should be 6
max_sum=arr[0]
curr_sum=arr[0]
for i in range(1,len(arr)):
    curr_sum=max(arr[i],curr_sum+arr[i])
    max_sum=max(arr[i],max_sum+curr_sum)
print(max_sum)

# this is only for finding the sum if we want to find the subarray then we have to go by if else condition inside for loop

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]    #[4, -1, 2, 1] final output should be 6
max_sum=arr[0]
curr_sum=arr[0]
start=0
end=0
temp_start=0
for i in range(1,len(arr)):
    if arr[i]>curr_sum:
        curr_sum=arr[i]
        temp_start=i
    else:
        curr_sum=curr_sum+arr[i]

    if max_sum<curr_sum:
        max_sum=max_sum+curr_sum
        start=temp_start
        end=i
print(arr[start:end+2])



