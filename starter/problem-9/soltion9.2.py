my_list = [4, 8, 7, 4,3,6,2,1,9]
found = False

for num in my_list:
    if num == 6:
        found = True
        break

if found:
    print("6 is in the list.")
else:
    print("6 is not in the list.")