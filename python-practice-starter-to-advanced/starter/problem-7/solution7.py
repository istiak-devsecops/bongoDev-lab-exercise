def fizzbuzz(num):
    if (num % 3 == 0) and (num % 5 == 0): #check if both is divisible by 3 and 5
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return "Not a FizzBuzz number!"


user_input = int(input("Write any number to know its a fizz buzz! "))

print(fizzbuzz(user_input))