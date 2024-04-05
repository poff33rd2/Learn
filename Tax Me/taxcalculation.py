#create a program that efficiently prints out the customers bill with tax
cost = input('What is the cost: ')
totalcost = float(cost)
tax_rate = 5.7

def billwtax(bill, tax):
    return round((bill * tax) / 100.00, 2)


print(billwtax(totalcost, tax_rate) + totalcost)