for i in range(0,4):
    for j in range(0,4):
        if i==1 and j==1:
            print(" ",end="")
        elif i==1 and j==2:
            print(" ",end="")
        elif i==2 and j==1:
            print(" ",end="")
        elif i==2 and j==2:
            print(" ",end="")
        else:
            print("*",end="")
    print()
