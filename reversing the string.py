#program to read the string and reverse the string
string=input("enter the string")
print("the",string,"in reverse order is")
length=len(string)
i=0
for a in range(-1,(-length-1),-1):
    print(string[i],"\t",string[a])
    i+=1
