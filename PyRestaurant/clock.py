employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

employeeid = input('Clock in by entering your Employee ID: ')

def get_employee_from_dict(id):
    return employee_dict[id]['name']


print('Your are now clocked in: ', get_employee_from_dict(int(employeeid)));

