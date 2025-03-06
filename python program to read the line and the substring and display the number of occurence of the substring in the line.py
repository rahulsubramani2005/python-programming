Line=input("enter the line")
sub=input("enter the sub string")
l=len(Line)
ls=len(sub)
start=count=0
end=l
while True:
    pos=Line.find(sub,start,end)
    if pos!=-1:
        count+=1
        start=pos+ls
    else:
        break
    if start>=l:
        break
print("the number of occurence of the substring in a line is",count)
