a = input("Enter the string: ")
length = len(a)
rev = -1
mid = length // 2  # Use integer division

for i in range(mid):
    if a[i] == a[rev]:# Compare characters from start and end
        rev -= 1  # Move reverse index
    else:
        print("The string is not a palindrome")
        break
else:
    print(a, "is a palindrome")
