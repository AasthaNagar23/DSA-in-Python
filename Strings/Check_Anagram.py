# Check Anagram
# listen and silent
a="listemn"
b="silennt"
c=0
count=0
if len(a)==len(b):
    for i  in a:
        if i not in b: 
            # above two lines are very important very very 
            c+=1
        else:
            count+=1
    if count==len(a):
        print("anagram")
    else:
        print("not anagram")
        

    
else:
    print("not anagram") 