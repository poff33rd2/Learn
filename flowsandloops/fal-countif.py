num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]
count = 0

def find_number_position(numbers):
    for index, number in enumerate(numbers):
        if number == 36:
            print('36 is in position: ', index)
            return
    print('number not found')

for i in num_list:
    count += 1
    if i > 45:
        print(i, ' over 45')
        # break
    elif i == 36:
        find_number_position(num_list)
    elif i < 45:
        print(i, ' under 45')

print(count)
    