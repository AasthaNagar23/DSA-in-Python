#insertion sort
arr = [5, 2, 4, 6, 1, 3]
for i in range(1,len(arr)):
    key=arr[i]  #current element
    j=i-1       #previous element
    while j>=0 and arr[j]>key:  #jab tak hum array ke under he and arr[j] ka value key se bada he 
        arr[j+1]=arr[j]         #hum arr[j+1] ko arr[j] value assign kardemge also j ka value minus kardenge
        j-=1
    arr[j+1]=key                #then key ka value hum update kardenge
print(arr)