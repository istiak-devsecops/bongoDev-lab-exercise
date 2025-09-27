dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

for key in dict1:
    if key in dict2:
        print(key, ":", dict1[key], ",", dict2[key])
