import random
rand = random.randrange(1,3)
move = input("Rock, Paper, or Scissors? ")
if move == "rock":
    move = 1
elif move == "paper":
    move = 2
elif move == "scissors":
    move = 3


elif move == rand:
    print("Tie!")
if move != rand:
    if ((move == 1) and (rand == 2)):
        print("You lost!")
    elif ((move == 2) and (rand == 3)):
        print("You lost!")
    elif ((move == 3) and (rand == 1)):
        print("You lost!")
    else:
        print("You won!")
