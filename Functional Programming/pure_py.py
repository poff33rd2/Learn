my_list = [1,2,3]

def add_to_list(lst, item):
    new_list = lst.copy()
    new_list.append(item)
    
    return new_list



print(add_to_list(my_list, 4))
print(my_list)
