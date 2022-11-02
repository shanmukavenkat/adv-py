##sum of odd numbers
# Take input from user.
num = int(input())

total = 0

for i in range(1, num + 1):

    # Check for even or not.
    if((i % 3) == 0):
        total = total + i

print( total)
