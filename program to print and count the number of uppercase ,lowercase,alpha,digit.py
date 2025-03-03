line=input("enter the line")
l=u=0
al=d=0
for a in line:
    if a.islower():
        l=l+1
    elif a.isupper():
        u=u+1
    elif a.isdigit():
        d=d+1
    if a.isalpha():
        al=al+1
    else:
        print("unauthorised character")
print("number of lowercase",l)
print("number of uppercase",u)
print("number of alphacase",al)
print("number of digitcase",d)
        
