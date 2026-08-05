# reversing array:
arr = list(map(int, input().split()))
if len(arr) == 0:
    print("No reversing")
else:
    arr.reverse()
    print(arr)