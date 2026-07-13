s="i am aastha nagar"
# Reverse Words in a String
a=s.split()
print(a)
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)
c=" ".join(b)  #important 
print(c)