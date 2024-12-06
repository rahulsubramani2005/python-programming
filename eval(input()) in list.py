'''while creating a list we can notice that always the output is in string even
if we give digits as input.in order to address this problem.
we use eval(input()) method'''

a=input("enter the sequence to be converted to list")
l=list(a)
lis=eval(input(l))
print(lis)
