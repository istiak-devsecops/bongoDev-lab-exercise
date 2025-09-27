secret_num = 6

while True:
    user_input = int(input("Guess the correct number 1 to 10: "))
    if user_input > secret_num:
        print("You are bit above than the number.")
    elif user_input < secret_num:
        print(" You are bit lower than the number.")
    else:
        print("you guess the right number.")
        break