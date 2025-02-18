print("the loop with break statement produce output as")
for i in range(1,11):
    if i%3==0:
        break
    else:
        print(i)
print("the loop with continue statement produces output as")
for i in range(1,11):
    if i%3==0:
        continue
    else:
        print(i)
