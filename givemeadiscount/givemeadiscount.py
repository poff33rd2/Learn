def get_total_cost():
    total_cost = 0 #set the variables before going into function
    isdonescanning = 'y'

    #while loop uses variables to signal whether or not a function continues
    while isdonescanning != 'n':
        itementry = input('enter the cost of the item: $')
        cost = float(itementry)
        total_cost += cost
        isdonescanning = input('Is there more items? (y/n): ')

#returns the variable as the data retreived at the end of using the function
    return total_cost


total_cost = get_total_cost() #intialize the function to run before doing everything else
loyalty = input('Are you are loyal member? (y/n)')
isloyalmember = (loyalty == 'y')

isdiscount = isloyalmember and total_cost > 50

if isdiscount: #defaults to checking if isdiscount is True
    discountbill = total_cost * .75
    total_bill = discountbill
else:
    total_bill = total_cost

print(f'Total bill: ${total_bill}')


#update this to accept new inputs until the user is done adding to eliminate hard coding which products are being purchased




