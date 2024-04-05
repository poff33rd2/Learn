#Sets: they don't allow duplicate values like lists
#Sets are collections of unordered items meaning we can't use this print(set_a[0]) to get the data in index 0

set_a = {1, 2, 3, 4, 5}
set_b = {6, 7, 8, 9, 10}
set_c = {1, 3, 5, 6}

# set_a.add(6) #adds 6 to the set
# set_a.remove(2) #removes 2 from the set

# allsets = set_a.union(set_b) #merges the sets into one
# allsets = set_a | set_b #does the same as ^^^^^^

# setintersect = set_a.intersection(set_c) #reveals the data that matches from set_a to set_c
# setintersect = set_a & set_c #does the same as ^^^^^^^

# setdiff = set_a.difference(set_c) #shows the values that are different found in set_a and not in set_c
# setdiff = set_a - set_c #does the same as ^^^^^

# setsym = set_a.symmetric_difference(set_c) #shows the difference that set_a and set_c has
# setsym = set_a ^ set_c #does the same as ^^^^^

print(set_a)

#sets are used to do mathematical operations