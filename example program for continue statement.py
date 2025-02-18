#example program for continue statement
a=b=c=0
for i in range(1,3):
    print("enter 2 numbers")
    a=int(input("enter number 1"))
    b=int(input("enter number 2"))
    if b==0:
        print("denominator cannot be zero!,enter again")
    else:
        c=a/b
        d=int(c)
        print("Quotien",c)
