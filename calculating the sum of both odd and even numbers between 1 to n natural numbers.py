#program to print and calculate the sum of both even and odd natural numbers between first and n natural numbers
n=int(input('enter upto which n natural numbers'))
sume=sumo=0
for i in range(1,n):
    if i%2==0:
        sume=sume+i
        print(i)
    else:
        sumo=sumo+i
print("the sum of even numbers is",sume)
print("the sum of odd numbers is",sumo)
