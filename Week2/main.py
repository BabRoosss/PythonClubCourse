import random
rand = random.randrange(1,100)
guess = int(input("Enter a number from 1 - 100: "))
while rand != guess:
    if guess < rand:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > rand:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("Yuppers!")
print()