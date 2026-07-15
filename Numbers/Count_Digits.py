a = int(input("Enter the number: "))
count=0
for i in range(a, 0, -1):
    print(i)
    count+=1
print("Total digits counted:", count)