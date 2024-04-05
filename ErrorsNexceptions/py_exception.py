def divideby(a, b):
    return a / b

#try and except statements carefully handles errors and display them instead of killing the application.
try: #it will try the code with the indent
    print(divideby(15, 0))
except Exception as e: #if the code in the try fails or an error occurs, it will print 'something went wrong' 'Exception' needs to be capitalized
    print('something went wrong: ', e) #prints the exception that occured
    print(e.__class__) #prints the class of error the exception is
except ZeroDivisionError as e: #erros can be specified before hand
    print(e, 'No numbers can be divided by Zero') #prints the exception that occured

#more than one except can be specified within one try : except : to be able to test more than one exception
#users error handlers allow developers to carefully catch errors and deliver them in a user-friendly way
