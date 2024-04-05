#args = can pass in any amount of non-keyword variables

# def sum_of(a, b): #accepts a set number of variables
#     return a + b

# print(sum_of(7, 5))

def sum_of(*args): #accepts any arguments to be made
    sum = 0

    for x in args:
        sum += x
    return sum

print(sum_of(4, 7, 7, 7))