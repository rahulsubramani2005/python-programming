#program to input some number repeatdly and print their sum.the program aborts when the number entered is less than zero
count=sum=0
ans='y'
while ans=='y':
    num=int(input("enter the number"))
    if num<0:
        print("numbers entered bellow is less than zero.Aborting")
        break
    sum=sum+num
    count=count+1
    ans=input("want to enter more numbers! y or n")
else:
    print("you entered",count,"numbers so far")
print("the sum of the entered numbers is",sum)
    
