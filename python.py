print("Welcome to the computer Quizz")

player = input("Do you want to play this Game? ")

if player != "yes":
    quit()

print("Lets start the game :) ")

score = 0

answer = input("What does the CPU stands for? ")
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does the GPU stands for? ")
if answer == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does the RAM stands for? ")
if answer == "random access memory":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("What does the PSU stands for? ")
if answer == "power supply unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("you got "+ str(score)+ " question correct!")

print("you got "+ str((score / 4) * 100)+ "%.")