arr = [1, 2, -3, -4]
arr1=[3,4,-5,-6]
arr2=[]
arr.sort()
arr1.sort()
arr2.sort()
a=set(arr)
b=set(arr1)
c=set(arr2)
d=a|b|c # important
e=list(d)
print(e)
