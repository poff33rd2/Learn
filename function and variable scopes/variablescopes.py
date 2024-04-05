#scope levels (LEGB): local scope, enclosing scope, global scope, built-in scope
#scopes are used to protect variables from being changed while the program is running

#global scope: accessible anywhere in the code -> can lead to mistakes in output
my_global = 10

def fn1():
    enclosed_v = 18 # this variable is accessible to all the code within this function from here to the bottom

    def fn2():
        local_v = 5 #this variable is not accesible to enclosed but accessible to all code wtihin the function on down

    print('global variable is: ', my_global) #This have access to enclosed and local
    print('access to enclosed: ', enclosed_v) #This have access to enclosed and local


fn1() #call fn1 

#reserve keywords: print and def has access at all levels of the code

#--Local scope----------------------------------

# def get_total(a, b):
#     #local variable declared inside a function
#     total = a + b;
#     return total

# print(get_total(5, 2))
# 7

# # Accessing variable outside of the function:
# print(total)
# NameError: name 'total' is not defined

#-----Enclosing scope----------------------------

# def get_total(a, b):
#     #enclosed variable declared inside a function
#     total = a + b

#     def double_it():
#         #local variable
#         double = total * 2
#         print(double)

#     double_it()
#     #double variable will not be accessible
#     print(double)

#     return total

#---Global scope----------------------------------

# special = 5

# def get_total(a, b):
#     #enclosed scope variable declared inside a function
#     total = a + b
#     print(special)

#     def double_it():
#         #local variable
#         double = total * 2
#         print(special)

#     double_it()

#     return total

#-----built-int scope---- rint, def, for, in