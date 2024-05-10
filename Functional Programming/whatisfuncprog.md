__functional programming__ - takes input and processes an output.

__Pure function__ - returns the same results and do the same thing.
• does not access or alter global scopes

#NOT PURE
global_list = [1, 2, 3]

def add_to(item):
    return global_list.append(item)

add_to(4)

print(global_list)

output: [1, 2, 3, 4]

#PURE: Extend the list as a argument, leave original list intact, return a new list

def add_to(global_list, item):
    new_list = global_list.copy
    new_list.append(item)
    return new_list

print(new_list)

Ensures the integrity of data within a application.
Changes in data can result in unwanted outputs.
Can Cache because return will never change.






__Traditional function__ - utilizes functions for clean, consistent, and maintable code. not changing any data outside of the function only returning the variable needed.

                        Traditional | Pure
access global state            y    |  n
modify global variables        y    |  n
access local state             y    |  y
change args                    y    |  n
output depends on input        n    |  y

