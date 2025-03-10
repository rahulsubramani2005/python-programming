s=input("enter the line")
s1=''
i=0
length=len(s)
end=length
while i < length:
    if i == 0:
        s1+=s[0].upper()
        i=i+1
    elif s[i] == ' ' and s[i+1] != ' ':
        s1+=s[i]
        s1+=s[i+1].upper()
        i=i+2
    else:
        s1+=s[i]
        i=i+1
print("orginal string",s)
print("the new string",s1)
