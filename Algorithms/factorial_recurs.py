
#NOT RECURSIVE
# def find_factorial_by_looping(n):
#     if n<0:
#         return 0
#     else:
#         factorial = 1
#         for i in range(1, n+1):
#             factorial = factorial*i
#         return factorial


# print(find_factorial_by_looping(5))


# def find_factorial_by_recursive(n):
#     if n == 1:
#         return 1
#     else:
#         return n * find_factorial_by_recursive(n - 1)
    
# print(find_factorial_by_recursive(1))

def tower_of_hanoi(disks, source, helper, destination):
    if(disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return
    
    tower_of_hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}'.format(disks, source, destination))
    tower_of_hanoi(disks -1, helper, source, destination)

disks = int(input('Number of disks to be moved: '))

print(tower_of_hanoi(disks, 'A', 'B', 'C'))

# print(tower_of_hanoi())