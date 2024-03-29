
runningshorts = input('$')
item1cost = int(runningshorts)

tracksocks = input('$')
item2cost = int(tracksocks)

beaniecap = input('$')
item3cost = int(beaniecap)

loyalty = input('Are you are loyal member? (y/n)')
isloyalmember = (loyalty == 'y')

bill = item1cost + item2cost + item3cost

isdiscount = isloyalmember and bill > 50

if isdiscount:
    discountbill = bill * .75
    total_bill = discountbill
else:
    total_bill = bill

print(f'Total bill: ${total_bill}')







