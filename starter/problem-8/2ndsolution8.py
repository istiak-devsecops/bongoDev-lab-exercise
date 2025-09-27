import random

secret_num = random.randint(1,10) # will pick a random number from 1 to 10

while True:
    #The loop will continue till user put the right number
    user_input = int(input("Guess the correct number from 1 to 10: "))
    if user_input > secret_num:
        print("You are above the correct number.")
    elif user_input < secret_num:
        print("You are below the correct number.")
    else:
        print("You guess the right number.")
        break
        


    

