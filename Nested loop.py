#Example program for nested loop
a=int(input("enter the number"))
for i in range(1,a):
    for j in range(1,i):
        print("*",end="")
    print()
