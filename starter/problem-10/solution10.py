data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

only_number = []

for num in data_list:
    if type(num) == int:
        only_number.append(num)


print(only_number)