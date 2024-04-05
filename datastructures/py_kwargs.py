#kwargs: allow pass in any amount of keyword arguments


def sum_of(**kwargs): #accepts any arguments to be made
    sum = 0

    for key, value in kwargs.items():
        sum += value
    return round(sum, 2)

print(sum_of(coffee=2.99, croissant=8.99))