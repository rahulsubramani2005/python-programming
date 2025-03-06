s1=input("enter the string")
le=len(s1)
a=0
end=le
s2=" "
while a<le:
    if a==0:
        s2+=s1[0].upper()
        a=a+1
    elif(s1[a]==" " and s1[a+1]!=" "):
        s2=s2+s1[a]
        s2+=s1[a+1].upper()
        a=a+2
    else:
        s2+=s1[a]
        a=a+1
print("Orginal String:",s1)
print("the captalize string",s2)
