n=int(input("enter the number"))
factorial=1
for i in range(1,n):

    temp=n-i
    factorial=factorial*temp
print("the factorial of ",n,"is",factorial)
