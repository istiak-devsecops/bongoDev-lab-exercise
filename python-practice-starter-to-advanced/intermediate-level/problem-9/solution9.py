def is_valid(password):
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password)

    return all([has_upper, has_lower, has_digit, has_special])

 
pwd = input("Enter password: ")
if is_valid(pwd):
    print("Password is valid")
else:
    print("Password is invalid")
