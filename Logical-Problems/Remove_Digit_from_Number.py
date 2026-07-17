# Remove Digit from Number
a=45783262548074398
b=str(a)
c=[]
for i in b:
    if i!="2":
       c.append(i) 
        
print(c)
d="".join(c)
print(d)