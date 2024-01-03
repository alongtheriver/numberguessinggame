import random

number = random.randrange(1,10)
guess = int(input("Choose number:"))

while number != guess:
    if guess < number:
        print("Too low")
        guess = int(input(("Enter the number")))

    elif guess > number:
        print("Too high")
        guess = int(input(("Enter the number")))

    else:
        break

    print("You guessed it right!")


