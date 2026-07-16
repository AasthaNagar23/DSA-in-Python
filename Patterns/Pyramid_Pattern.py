row=5
column=5
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()