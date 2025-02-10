a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
min=mid=max=None
if a<b and a<c:
    if b<c:
        min,mid,max=a,b,c
    else:
        min,mid,max=a,c,b
elif b<a and b<c:
    if a<c:
        min,mid,max=b,a,c
    else:
        min,mid,max=b,c,a
else:
    if b<a:
        min,mid,max=c,b,a
    else:
        min,mid,max=c,a,b
print("Numbers in Ascending Order.",min,mid,max)
