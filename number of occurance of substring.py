line=input("enter the line")
sub=input("enter the substring")
length=len(line)
lensub=len(sub)
start=0
count=0
end=length
while True:
    pos=line.find(sub,start,end)
    if pos != -1:
        count+=1
        start=pos + lensub
    else:
        break
    if start >= length:
        break
print("No.of occurance of",sub,':',count)
