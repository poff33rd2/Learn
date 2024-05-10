# list comprehensions provide a concise/cleaner way to deal with looping and manipulating lists []

#PRACTICE 1
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# # loop 1: x for x in fruits - initiates x for items in list-fruits 
# # loop 2: if 'a' in x - new list will contain all list items that has 'a'

# print(newlist)


#PROBLEM 1: list comprehension
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
    
#     # cuboid coordinates: (i, j, k) - (a, b, c)
#     #print in lexiographic [0, 0, 1] [0, 1, 0]
#     #list comprehension
#     #sum can't equal n
#     #maximum range is 1 - coordinates between 0 and 1

    
# posscordinates = [[i, j, k] for i in range(x + 1) for  j in range(y + 1) for k in range(z + 1) if i + j + k != n]

# print(posscordinates)

# #PROB 2: Dictionary Comprehension
# usingrange = {x:x*2 for x in range(12)}
# print("Using range(): ",usingrange)


# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]

# numdict = {x:x**2 for x in number}
# print("Using one input list to create dict: ", numdict)

# months_dict = {key:value for (key, value) in zip(number, months)}
# print("Using two lists: ", months_dict)


#Prob 3: Set comprehension
# set_a = {x for x in range(10,20) if x not in [12,14,16]}
# print(set_a)


# Prob 4: Generator comprehension
# data  = [2,3,5,7,11,13,17,19,23,29,31]

# gen_obj = (x for x in data)
# print(gen_obj)
# print(type(gen_obj))
# for items in gen_obj:
#     print(items, end=' ')

#Notice how both map() functions and list comprehension effectively do the same job of modifying iterator sequences such as the list in the example above.

# z = ["alpha","bravo","charlie"]
# new_z = [i[0]*2 for i in z]
# print(new_z)

a = [[96], [69]]

print(''.join(list(map(str, a))))