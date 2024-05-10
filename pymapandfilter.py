menu = ['espresso', 'mocha', 'latte', 'cappuccino', 'cortado', 'americano']

def find_coffee(coffee):
    if coffee[0] == 'c' : 
        return coffee
    


map_coffee = map(find_coffee, menu) #takes all objects of a list and applies a function
print(map_coffee)
for x in map_coffee:
    print(x)

# filter_coffee = filter(find_coffee, menu) #does the same as map but takes the results and creates a new list with only the true values.
# print(filter_coffee)
# for x in filter_coffee:
#     print(x)


# a = [[96],[69]]
# print(''.join(list(map(str, a))))