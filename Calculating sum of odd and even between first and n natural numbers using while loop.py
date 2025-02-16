#program to print and calculate sum of first and n natural numbers using while loop
n=int(input('enter upto which natural number'))
a=1
sume=sumo=0
while(n>=a):
    if(a%2==0):
        sume=sume+a
    else:
        sumo=sumo+a
    a=a+1
print("the sum even first and n natural numbers is",sume)
print("the sum odd first and n natural numbers is",sumo)
