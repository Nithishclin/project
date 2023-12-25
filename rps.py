import random  # import random module in python

user_wins = 0  # to determine the score for user
computer_wins = 0  # to determine the score for computer

option = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type rock/paper/scissor or Q for quit: ").lower()
    if user_input == "q":
        break

    if user_input not in option:
        continue

    random_pick = random.randint(0,2)
    computer_pick = option[random_pick]
    print("computer pick", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("you win!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("you win!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("you win!")
        user_wins += 1
    else:
        print("computer won!")
        computer_wins += 1

u_win = "you won", user_wins,"times."
c_win = "Computer won", computer_wins,"times."
print(u_win)
print(c_win)

if user_wins > computer_wins :
    print("Your score is higher than computer, So You are the WINNER!!")
else:
    print("Computer score is higher than your's , So Computer is the WINNER!!")

