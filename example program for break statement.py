a=b=c=0
for i in range(1,21):
    a=int(input("enter number 1"))
    b=int(input("enter number 2"))
    if b==0:
        print("Division by zero is error!")
        break
    else:
        c=a/b
        print("Quotient",c)
