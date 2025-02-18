#python program to implement guess the number game with 10 attempts

import random
n = random.randint(10,50)
a=0
while a<5:
    guess=int(input("enter the number"))
    if guess == n:
        print("You Won")

        break
    else:
        a=a+1
if not a<0:
    print("you lose : \n The number was",n)
