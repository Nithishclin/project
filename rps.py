import random  # import random module in python

user_wins = 0  # to determine the score for user
computer_wins = 0  # to determine the score for computer

option = ["rock", "paper", "scissor"]  # option for the user

while True:  # to start the loop
    user_input = input("Type rock/paper/scissor or Q for quit: ").lower()  # Ask the user to type rock/paper/scissor or Q.
    if user_input == "q":
        break  # if the user type "Q" the code stop here and start from the loop again

    if user_input not in option:
        continue  # if user answer not in the option variable {rock,paper,scissor} ,it continues again from user input

    random_pick = random.randint(0,2)  # set a random pick from index 0 to 2
    computer_pick = option[random_pick]  # in this comment random pick from the option variable {rock=0, paper=1, scissor-2}
    print("computer pick", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":  # if user pick rock and computer pick scissor , the user win
        print("you win!")
        user_wins += 1  # to increase user_wins
    elif user_input == "paper" and computer_pick == "rock":  # if user pick paper and computer pick rock , the user win
        print("you win!")
        user_wins += 1  # to increase user_wins
    elif user_input == "scissor" and computer_pick == "paper":  # if user pick scissor and computer pick paper , the user win
        print("you win!")
        user_wins += 1  # to increase user_wins
    else:
        print("computer won!")  # if the above are false the computer wins
        computer_wins += 1  # to increase computer_wins


print("you won", user_wins, "times.")
print("Computer won", computer_wins, "times.")

if user_wins > computer_wins:  # if the user score more points than computer, it prints the below statement
    print("Your score is higher than computer, So You are the WINNER!!")
else:  # if the computer score more points than user, it prints the below statement
    print("Computer score is higher than your's , So Computer is the WINNER!!")

