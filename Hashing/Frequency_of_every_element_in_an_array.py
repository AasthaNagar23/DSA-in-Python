# Frequency of every element in an array
arr = [1,2,3,4,5,2,0,3,4]

freq = {}

for i in arr:
    if i in freq:
        freq[i] += 1  #means value stored for the i should be increased by one 
    else:             #as hum frequency par kaam kar rhe he 
        freq[i] = 1

for key in freq:
    print(key, "->", freq[key])