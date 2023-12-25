

import random  # import random function for import random number

top_of_range = input("Typer a Number ")  # allow the user to type a number to set range

if top_of_range.isdigit():
    top_of_range = int(top_of_range)  # to check the input is a number

    if top_of_range <=0:
        print("Please type a number larger than 0 ")  # ask the user to type larger number
        quit()  # quit from the program

else:
    print("please type a number")  # if the user type a character in input type
    quit()  # quit from the program

random_number = random.randint(0 ,top_of_range)  # print a random number in particular range according to user input

guesses = 0  # no of the time user guessing the answer

while True:  # while condition used for loop the program
    guesses += 1
    user_guess = input("Gress a Number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)  # to check the input is a number
    else:
        print("Please type a number")  # if the user type a character in input type
        continue  # continue condition use to start from the beginning and leave the else statement


    if user_guess == random_number:  # when a user input and random value are equal
        print("You got it right")
        break
    else:
        if user_guess > random_number:  # when the user input is larger than random value
            print("you were above the number")
        else:  # when the user input is smaller than random value
            print("you were below the number")

print("you got it in", guesses,"guesses")








