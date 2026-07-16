row=5
column=5
for i in range(row,-1,-1):
    for j in range(i):
        print(" ",end=" ")
    for j in range(column-i):
        print("*",end=" ")
    print()

#pehle stars print karo and then n-i jitna spaces print karo but isme ulta ho jaega 
#just know the concept of it 