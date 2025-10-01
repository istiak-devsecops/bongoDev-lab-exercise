def find_missing(logs):
    n = len(logs) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(logs)
    return expected_sum - actual_sum

# Example
logs = [1, 2, 4, 5]
print(find_missing(logs))  
 