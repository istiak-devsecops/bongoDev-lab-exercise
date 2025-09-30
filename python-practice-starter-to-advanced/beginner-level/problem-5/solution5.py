lists = [1, [2, 3], [4, [5]]]

def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):   # check if it's a sublist
            result.extend(flatten(item))  # recursively flatten
        else:
            result.append(item)
    return result

print(flatten(lists))