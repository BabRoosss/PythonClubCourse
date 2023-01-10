import random
rand = random.randrange(1,3)
MOVE = input("Rock, Paper, or Scissors? ")
if MOVE == "rock":
    MOVE = 1
elif MOVE == "paper":
    MOVE = 2
elif MOVE == "scissors":
    MOVE = 3


if MOVE == rand:
    print("Tie!")
elif MOVE != rand:
    if ((MOVE == 1) and (rand == 2)):
        print("You lost!")
    elif ((MOVE == 2) and (rand == 3)):
        print("You lost!")
    elif ((MOVE == 3) and (rand == 1)):
        print("You lost!")