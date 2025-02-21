# Number of lines in the pattern
lines = 4

# Outer loop for the number of lines
for i in range(lines, 0, -1):
    # Inner loop to print stars on each line
    for j in range(i):
        print('*', end='')
    print()  # Move to the next line after printing stars
