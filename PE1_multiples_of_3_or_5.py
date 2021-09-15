# Project Euler - Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# check if int is a multiple of 3
def check_multiple_3(x):
    if x % 3 == 0:
        return True
    else:
        return False
    return

# check if int is a multiple of 5
def check_multiple_5(x):
    if x % 5 == 0:
        return True
    else:
        return False
    return

total = 0

for i in range(1,1000):
    if check_multiple_3(i) or check_multiple_5(i):
        total += i

print(total,i)