# finding index of the element:
arr=list(map(int, input().split()))
target=2
if len(arr)==0:
    print("-1")
else:
    for i in range(len(arr)):
        if arr[i]==target:
            print(i, end=" ")
if target not in arr:
    print("-1")
