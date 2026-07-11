arr= [1, 2, 3, 4, 5]  #[2,3,4,5,1]
a=arr[0]
b=arr[1]
arr.remove(arr[0])
arr.remove(arr[0])
arr.append(a)
arr.append(b)
print(arr)            #Right Rotate Array by One will be of the same process
