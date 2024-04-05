#---list w/ int---
intlist = [1, 2, 3, 5]

#---string list---
strlistt = ['A', 'B', 'C']

#---Basic List with Mixed Data Types---
mixed_list = [42, 3.14, 'hello world', True]

#---List Containing Lists (Nested Lists)---
nested_list = [[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']]

#---print list---
print(*intlist) #prints 1 2 3 5

print(intlist, sep= ' ' ) #prints [1, 2, 3, 5]

print(intlist[1]) #prints 2

#---add items to list---
intlist.insert(len(intlist), 6) #adds 6 to the intlist
intlist.append(6) #same as ^^^^^^^
intlist.extend([6, 7, 8, 9]) #adds the list to intlist

#---remove items from list---
intlist.pop(3) #goes the index 3 which is 5, then removes it.
del intlist[3] #does the same as ^^^^^^^^^^

