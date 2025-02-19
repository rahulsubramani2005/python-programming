#program to input a number and test if it is a primenumber
num=int(input("enter the number"))
lim=int(num/2)+1
for i in range(2,num):
    rem=num%i
    if rem==0:
        print(num,"is not a primenumber")
        break
else:
    print(num,"it is a primenumber")
