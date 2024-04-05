- syntax errors are human made like forgeting : or mispelling

- known errors that need to be handled are exceptions
can easily be uncaught by human, need to be handled by by the developer.
i.e.: a = 5 / 0 - terminal will through an error 

-Generic Try and except handle:
Try:
Except:

-give except specification
Try:
###code
except Exception as e: #Exception has to be capitalized
###code 

-Handle multiple exception in one try handle:
Try:
###code to be handled
Except Exception as e:
print('Error message', e)
Except: #second exception to be fired when the above exception does not fit users error
###code

Use error handling where known and possible errors can occur from the user.
