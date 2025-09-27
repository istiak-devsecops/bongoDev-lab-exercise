list1 = [3, 5, 7, 4, 8, 8]

list2 = [4, 9, 8, 7, 1, 1, 13]

new_list = []

for num in list1:
    if num in list2:
        new_list.append(num)

print(f'common iteams in both lists are {new_list}')
print(f'sum of every common items {sum(new_list)}')