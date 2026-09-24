# Reorder the following lines of code so that it prints 0 through n
# unless the number is divisible by x, then print fizz
# or if it's divisible by y, then print Buzz
# or if it's divisible by both, print Fizzbuzz


n = 10
y = 2
x = 3


for i in range(n):          # line g
    if i % (x * y) == 0:    # line c
        print("Fizzbuzz")   # line f
    elif i % x == 0:        # line a
        print("Fizz")       # line b
    elif n % y == 0:        # line h
        print("Buzz")       # line e
    else:                   # line d
        print(i)            # line k