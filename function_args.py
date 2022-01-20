# *args  COME AS TUPLES
# CAN PUT UNLIMITED AMOUNT OF ARGS
from audioop import add

# IN JAVASCRIPT 
# add_numbers(...args)

def add_numbers(*args):
    total = 0
    # print(args)
    # print(type(args))       # TUPLE
    for num in args:
        total += num
    return total

total = add_numbers(1,2,3,4)
print(total)