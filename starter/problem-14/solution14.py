list_1 = [4, 9, 8, 7, 5, 2, 13]

list_1.sort()       # Sort ascending
list_1 = list_1[::-1]  # Reverse using slicing

print("Sorted Descending:", list_1)
print("Difference (Max - Min):", list_1[0] - list_1[-1])