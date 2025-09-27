first_brother = 28
second_brother = 21

def age_counter(a,b):
    if a > b:
        return "first brother is older"
    elif b > a:
        return "second brother is older"
    else:
        return "The are the same age"
    
result = age_counter(first_brother,second_brother)

print(result)