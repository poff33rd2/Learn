# The below script will ask for 3 inputs. Each input will be based
# on the price of the items - the price is determined by you. The output
# should print the total of the 3 inputs rounded to 2 decimal places e.g
#
#   1 coffee @ $ 2.00
#   1 sandwich @ $ 4.99
#   1 cake @ $ 2.75
#
#   Your total bill is $ 9.74

# Modify the line below
coffeeinput = input('1 coffee @: $ ')
coffee = float(coffeeinput)

# Modify the line below
sandwichinput = input('1 sandwich @: $ ')
sandwich = float(sandwichinput)

# Modify the line below
cakeinput = input('1 cake @: $ ')
cake = float(cakeinput)


bill_total = coffee + sandwich + cake

# total_usround = float(bill_total)

print('Your total bill is $', bill_total)