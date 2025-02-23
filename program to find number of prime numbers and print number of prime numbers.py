#program to print the primenumbers and their count within the range
a=int(input("enter the starting point more than 1"))
b=int(input("enter the ending point"))
count=0
for i in range(a,b):
    for j in range(2,i):
        if i%j==0:
            fact=i/j
            fact=int(fact)
            print("found a factor (",fact,") for",i)
            break
        
    else:
        print("it is prime number",i)

            
