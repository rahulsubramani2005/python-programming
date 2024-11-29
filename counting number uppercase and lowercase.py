line=input("enter the line")
lowercount=0
uppercount=0
digitcount=0
alphacount=0
for a in line:
    if a.islower():
        lowercount+=1
    elif a.isupper():
        uppercount+=1
    elif a.isdigit():
        digitcount+=1
    if a.isalpha():
        alphacount+=1
print("Number of lowercase letters in line",lowercount)
print("Number of uppercase letters in line",uppercount)
print("Number of digitcase letters in line",digitcount)
print("Number of alphacase letters in line",alphacount)
